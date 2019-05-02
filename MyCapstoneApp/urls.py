from django.urls import path

from . import views

urlpatterns = [
    # ex: /track/
    path('', views.index, name='index'),
    # ex: /track/5/
    path('<int:school_id>/', views.school_detail, name='detail'),
    # ex: /track/5/athletes/
    path('<int:school_id>/athletes/', views.school_athletes, name='athletes'),
]