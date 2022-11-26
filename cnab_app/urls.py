from django.urls import path
from . import views

urlpatterns = [
    path("cnab/", views.CnabView.as_view()),
    path("cnab/filter/", views.SearchMovementOfOneStoreView.as_view()),
]
