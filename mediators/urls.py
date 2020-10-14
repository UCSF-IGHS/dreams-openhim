from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('echo/', views.EchoAPIView.as_view()),
]