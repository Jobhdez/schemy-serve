from src.compilers.scm_interpreter.parser import scmparser 
from src.compilers.scm_interpreter.interp import interp
from .models import SchemeInterpreter, Challenges
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
    )
from .serializers import SchemeInterpSerializer, ChallengesSerializer
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
    challenge = Challenges(problem_statement=data["problem_statement"], solution=data["solution"])
    challenge.save()
    user = request.user 
    user.challenges.add(challenge)

    return Response({"challenge": "created"}, status=200)

@api_view(['GET'])
def challenge_listing(request):
  challenges = Challenges.objects.all()
  serializer = ChallengesSerializer(challenges, many=True)
  return Response(serializer.data)
