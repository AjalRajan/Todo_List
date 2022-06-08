
from django.urls import path
from todo import views

urlpatterns = [
    path('home/' , views.home),
    path('addtodo/' , views.addtodo),
    path('deletetodo/<int:iteam_id>/' , views.deletetodo),
]
