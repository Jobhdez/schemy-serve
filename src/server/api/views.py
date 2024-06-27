from src.compilers.scm_interpreter.parser import scmparser 
from src.compilers.scm_interpreter.interp import interp
from .models import (
  SchemeInterpreter,
  Challenges,
  ProblemStatement,
  Solution,
  SchemeApp,
  )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import (
    authenticate,
    login,
    get_user_model,
    )
from .forms import (
    CompilerForm,
    UserRegistrationForm,
    UploadSchemeFile,
    ChallengesForm,
    ProblemForm,
    SchemeAppForm,
    )
from .serializers import (
  SchemeInterpSerializer,
  ChallengesSerializer,
  ProblemStatementSerializer,
  SolutionSerializer,
  SchemeAppSerializer,
  UserSerializer,
  )
import io
User = get_user_model()

@api_view(['POST'])
def register(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        data = form.cleaned_data
        new_user.set_password(data['password'])
        new_user.save()

        return Response({'account':'created'})

    return Response({'form':'invalid'})

@api_view(['POST'])
def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"login": "successful"})
        return Response({"create": "account"})
    return Response({'form': 'invalid'})

@api_view(['POST'])
@login_required(login_url='/api/login')
def scheme_interpreter(request):
    form = CompilerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        exp = data['input_expression']
        parsed_exp = scmparser.parse(exp)
        evaluation = interp(parsed_exp)
        scm_model = SchemeInterpreter(input_expression=data['input_expression'], output_expression=evaluation)
        scm_model.save()
        user = request.user
        user.scm_interp_exps.add(scm_model)
        serializer = SchemeInterpSerializer(scm_model)
        return Response(serializer.data)
    return Response({'form':'invalid'})

@api_view(['POST'])
@login_required(login_url='/api/login')
def evaluate_scm_from_file(request):
    form = UploadSchemeFile(request.POST, request.FILES)
    scm_file = request.FILES['scm_file']
    scm_exp = scm_file.file
    bytes_data = scm_exp
    scm_exp = bytes_data.read().decode('utf-8')
    parsed_exp = scmparser.parse(scm_exp)
    evaluation = interp(parsed_exp)
    scm_model = SchemeInterpreter(input_expression=scm_exp, output_expression=evaluation)
    scm_model.save()
    user = request.user
    user.scm_interp_exps.add(scm_model)
    serializer = SchemeInterpSerializer(scm_model)
    return Response(serializer.data)

@api_view(['GET'])
@login_required(login_url='/api/login')
def scheme_expressions(request):
    usr = request.user
    exps = usr.scm_interp_exps.all()
    serializer = SchemeInterpSerializer(exps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required(login_url='/api/login')
def scheme_expression(request, id):
    usr = request.user
    exp = usr.scm_interp_exps.get(id=id)
    serializer = SchemeInterpSerializer(exp)
    return Response(serializer.data)

@api_view(['POST'])
@login_required(login_url='/api/login')
def challenge(request):
  form = ChallengesForm(request.POST)
  if form.is_valid():
    data = form.cleaned_data
    challenge = Challenges(name=data["name"])
    challenge.save()
    problem = ProblemStatement(problem_statement=data['problem_statement'])
    problem.save()
    challenge.problem_statement.add(problem)
    solution = Solution(solution=data['solution'])
    solution.save()
    challenge.solution.add(solution)
    challenge.save()
    user = request.user 
    user.challenges.add(challenge)

    user.save()
    return Response({"challenge": "created"}, status=200)

@api_view(['POST'])
@login_required(login_url='/api/login')
def add_problem(request):
  form = ProblemForm(request.POST)
  if form.is_valid():
    data = form.cleaned_data
    challenge = request.user.challenges.get(id=data['challenge_id'])
    problem = ProblemStatement(problem_statement=data['problem'])
    problem.save()
    challenge.problem_statement.add(problem)
    solution = Solution(solution=data['solution'])
    solution.save()
    challenge.solution.add(solution)
    challenge.save()
    return Response({"problem-solution": "added"}, status=200)
                                                         
@api_view(['GET'])
def challenge_listing(request):
  challenges = Challenges.objects.all()
  serializer = ChallengesSerializer(challenges, many=True)
  return Response(serializer.data)

def challenge_detail(request, id):
  return Response(ChallengesSerializer(Challeges.objects.get(id=id)).data)

@api_view(['GET'])
@login_required(login_url='/api/login')
def user_challenges(request):
  user = request.user
  challenges = user.challenges.all()
  return Response(ChallengesSerializer(challenges, many=True).data)
  
#to do
# challenge_detail
# challege_delete

@api_view(['POST'])
@login_required(login_url='/api/login')
def create_app(request):
  scm_app = SchemeApp(owner=request.user)
  scm_app.save()
  return Response({"app": "created"})

@api_view(['POST'])
@login_required(login_url='/api/login')
def add_user_to_app(request):
  form = SchemeAppForm(request.POST)
  if form.is_valid():
    data = form.cleaned_data
    app = SchemeApp.objects.get(id=data['app_id'])
    if app.owner == request.user:
      app_user = User.objects.get(username=data['username'])
      app.users.add(app_user)
      app.save()
      return Response({"success": "user added to app"}, status=200)
    return Response({"failure":"you need to be the owner of the app"}, status=303)

  return Response({"form":"invalid"})

@api_view(['GET'])
@login_required(login_url='/api/login')
def get_app_users(request, app_id):
                                  
  app = SchemeApp.objects.get(id=app_id)
  if app.owner == request.user:
    serializer = UserSerializer(app.users, many=True)
    return Response(serializer.data)
  return Response({"failure": "you need to be the owner"}, status=303)

