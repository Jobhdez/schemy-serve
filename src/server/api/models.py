from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    scm_interp_exps = models.ManyToManyField("SchemeInterpreter")
    challenges = models.ManyToManyField("Challenges")
    friends = models.ManyToManyField("User", blank=True)
    class Meta:
        app_label = 'api'

class SchemeApp(models.Model):
    users = models.ManyToManyField("User", related_name="scheme_apps")
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_apps")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'This app is owned by: {self.owner.username}'
  
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
        ordering = ['created']

    def __str__(self):
        return f'the problem statement: {self.problem_statement}'

class Solution(models.Model):
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'the solution: {self.solution}'

class Competition(models.Model):
  challenge = models.ManyToManyField("Challenges")
  challenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="challenger")
  opponent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="opponent")
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return f'competition between user {self.challenger.username} and {self.opponent.username}'

class Points(models.Model):
  points = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_points")

  class Meta:
    ordering = ['created']

  def __str__(self):
    return f'user {self.user.username} has {self.points} points'

class FriendRequest(models.Model):
    """Class that enables a connection between two users."""
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.from_user} wants to befriend {self.to_user}.'


class CompetitionRequest(models.Model):
    """Class that enables a connection between two users."""
    from_user = models.ForeignKey(User, related_name='compete_from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='compete_to_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.from_user} wants to compete with {self.to_user}.'
  
