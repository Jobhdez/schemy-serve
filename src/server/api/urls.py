from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('scm_exps/', views.scheme_interpreter, name='scm_exps'),
    path('scm_uploads/', views.evaluate_scm_from_file, name='upload_scm'),
    path('scm_expressions/', views.scheme_expressions, name='scm_exprs'),        
    path('scm_exp/<int:id>/', views.scheme_expression, name='scm_exp'),
    path('challenge/', views.challenge, name='challenge'),
    path('challenges/', views.challenge_listing, name='challenges'),
    path('users/challenges/', views.user_challenges, name='user_challenges'),
    path('users/challenges/problems/', views.add_problem, name='user_problem'),
    path('users/apps/', views.create_app, name='app'),
    path('users/apps/users/user/', views.add_user_to_app, name='user_addition'),
    path('users/apps/users/<int:app_id>/', views.get_app_users, name="get_app_users"),
    ]
