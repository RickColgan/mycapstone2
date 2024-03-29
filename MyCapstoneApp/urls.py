from django.urls import path

from . import views

app_name = 'MyCapstoneApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/athletes/', views.AthletesView.as_view(), name='athletes'),
    ]