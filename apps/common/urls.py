from django.urls import path
from apps.common import views

urlpatterns = [
    path("blank/", views.CreateBlankView.as_view()),
]

