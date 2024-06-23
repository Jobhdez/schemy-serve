from rest_framework import serializers
from .models import SchemeInterpreter, Challenges, ProblemStatement, Solution

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
