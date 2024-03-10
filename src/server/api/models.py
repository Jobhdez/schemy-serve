from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    lalg_interp_exps = models.ManyToManyField("LinearAlgebraInterpreter")
    lalg_compile_exps = models.ManyToManyField("LinearAlgebraCompiler")
    scm_interp_exps = models.ManyToManyField("SchemeInterpreter")
    
class Compiler(models.Model):

    input_expression = models.CharField(max_length=200)
    output_expression = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class LinearAlgebraInterpreter(Compiler):

    def __str__(self):
        return f'Linear Algebra Interpreter with input {self.input_expression} and evaluated code {self.output_expression}'

class LinearAlgebraCompiler(Compiler):

    def __str__(self):
        return f'Linear Algebra Compiler with input {self.input_expression} and generated C code {self.output_expression}'

class SchemeInterpreter(Compiler):

    def __str__(self):
        return f'The Scheme expression {self.input_expression} is evaluated to {self.output_expression}'
