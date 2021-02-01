from django.urls import path

from mediators.views.dreams_intervention_mediator_api_view import DreamsInterventionMediatorAPIView
from mediators.views.echo_api_view import EchoAPIView
from mediators.views.index_view import IndexView
from mediators.views.register_dreams_intervention_mediator_api_view import RegisterDreamsInterventionMediatorAPIView
from mediators.views.register_echo_api_view import RegisterEchoAPIView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register-echo-mediator/', RegisterEchoAPIView.as_view()),
    path('echo/', EchoAPIView.as_view()),

    path('register-dreams-odk-mediator/', RegisterDreamsInterventionMediatorAPIView.as_view()),
    path('dreams-odk-intervention/', DreamsInterventionMediatorAPIView.as_view()),
]
