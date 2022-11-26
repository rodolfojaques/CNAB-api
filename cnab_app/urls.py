from django.urls import path
from . import views

urlpatterns = [
    path("cnab/", views.CnabView.as_view()),
]
