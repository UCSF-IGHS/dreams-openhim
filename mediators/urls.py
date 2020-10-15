from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register-echo-mediator/', views.RegisterEchoAPIView.as_view()),
    path('echo/', views.EchoAPIView.as_view()),

    path('register-dreams-odk-mediator/', views.RegisterDreamsInterventionMediatorAPIView.as_view()),
    path('dreams-odk-intervention/', views.DreamsInterventionMediatorAPIView.as_view()),
]