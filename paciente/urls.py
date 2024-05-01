from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('escolher_horario/<int:id_dados_medicos>', views.escolher_horario, name="escolher_consulta"), 
    path('agendar_horario/<int:id_data_aberta>/', views.agendar_horario, name="agendar_horario"),
    path('minhas_consultas/', views.minhas_consultas, name="minhas_consultas"),
    path('consulta/<int:id_consulta>/', views.consulta, name="consulta"),
<<<<<<< HEAD
    path('cancelar_consulta/<int:id_consulta>/', views.cancelar_consulta, name="cancelar")
=======
>>>>>>> d520939546067e8087767960f5c89772f547ed44
]

