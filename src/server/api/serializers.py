from rest_framework import serializers
from .models import SchemeInterpreter, Challenges 

class SchemeInterpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeInterpreter
        fields = ['input_expression', 'output_expression', 'created']

class ChallengesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Challenges
    fields = ['problem_statement', 'solution']
