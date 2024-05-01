from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('cadastro/', views.cadastro, name="cadastro"),
=======
    path('cadastro/', views.cadastro, name = "cadastro"),
>>>>>>> d520939546067e8087767960f5c89772f547ed44
    path('login/', views.login_view, name="login"),
    path('sair/', views.sair, name="sair")
]