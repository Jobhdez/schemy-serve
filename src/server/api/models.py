from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    scm_interp_exps = models.ManyToManyField("SchemeInterpreter")
    challenges = models.ManyToManyField("Challenges")
    class Meta:
        app_label = 'api'
        
class Compiler(models.Model):

    input_expression = models.CharField(max_length=200)
    output_expression = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class SchemeInterpreter(Compiler):

    def __str__(self):
        return f'The Scheme expression {self.input_expression} is evaluated to {self.output_expression}'

class Challenges(models.Model):
  problem_statement = models.ManyToManyField("ProblemStatement")
  solution = models.ManyToManyField("Solution")
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=200)
  class Meta:
    ordering = ['created']
    
  def __str__(self):
    return f'The problem statement: {self.name}'

class ProblemStatement(models.Model):
  problem_statement = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering=['created']

  def __str__(self):
    return f'the problem statement: {self.problem_statement}'


class Solution(models.Model):
  solution = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering=['created']

  def __str__(self):
    return f'the solution: {self.problem_statement}'

