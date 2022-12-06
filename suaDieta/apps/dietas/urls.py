from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('teste', teste, name="teste"),
    path('forms', forms, name="forms"),
    path('<int:dieta_id>/change-dieta', change_dieta, name="change_dieta"),
    path('<int:dieta_id>/delete-dieta', delete_dieta, name="delete_dieta"),
    path('<int:dieta_id>/view-dieta', view_dieta, name="view_dieta"),
    path('dashboard', dashboard, name="minhas_receitas")
]


