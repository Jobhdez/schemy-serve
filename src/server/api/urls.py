from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    #path('lalg_interp_exps/', views.linear_algebra_interp, name='lalg_exps'),
    #path('lalg_compile_exps/', views.linear_algebra_compiler, name='lalg_comp_exps'),
    path('scm_exps/', views.scheme_interpreter, name='scm_exps'),
    ]
