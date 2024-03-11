from rest_framework import serializers
from .models import SchemeInterpreter

class SchemeInterpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeInterpreter
        fields = ['input_expression', 'output_expression', 'created']
