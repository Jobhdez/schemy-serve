from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    scm_interp_exps = models.ManyToManyField("SchemeInterpreter")
    
    class Meta:
        app_label = 'api'
        
class Compiler(models.Model):

    input_expression = models.CharField(max_length=200)
    output_expression = models.CharField(max_length=200)
    #price = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class SchemeInterpreter(Compiler):

    def __str__(self):
        return f'The Scheme expression {self.input_expression} is evaluated to {self.output_expression}'
