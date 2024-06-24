from rest_framework import serializers
from .models import SchemeInterpreter, Challenges, ProblemStatement, Solution, User, SchemeApp

class SchemeInterpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeInterpreter
        fields = ['input_expression', 'output_expression', 'created']

class ProblemStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatement
        fields = ['problem_statement', 'created']

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['solution', 'created']

class ChallengesSerializer(serializers.ModelSerializer):
    problem_statement = ProblemStatementSerializer(many=True, read_only=True)
    solution = SolutionSerializer(many=True, read_only=True)

    class Meta:
        model = Challenges
        fields = ['problem_statement', 'solution', 'created']

class UserSerializer(serializers.ModelSerializer):
  scm_interp_exps = SchemeInterpSerializer(many=True, read_only=True)
  challenges = ChallengesSerializer(many=True, read_only=True)
  class Meta:
    model = User
    fields = ['scm_interp_exps', 'challenges', 'first_name', 'username', 'email']

class AppSerializer(serializers.ModelSerializer):
  users = UserSerializer(many=True, read_only=True)
  owner = UserSerializer(read_only=True)
  class Meta:
    model = SchemeApp
    fields = ['users', 'owner', 'created']
