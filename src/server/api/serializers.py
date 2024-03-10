from rest_framework import serializers
from .models import (
    LinearAlgebraCompiler,
    LinearAlgebraInterpreter,
    SchemeInterpreter,
    )

class LinearAlgebraInterpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearAlgebraInterpreter
        fields = ['input_expression', 'output_expression', 'created']

class LinearAlgebraCompilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearAlgebraCompiler
        fields = ['input_expression', 'output_expression', 'created']
        
class SchemeInterpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeInterpreter
        fields = ['input_expression', 'output_expression', 'created']
