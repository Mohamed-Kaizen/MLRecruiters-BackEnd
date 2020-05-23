"""users REST API URL Configuration"""

from django.urls import path
from .views import WorkerListAPI, CareerListAPI, WorkerRetrieveUpdateAPI
app_name = "users"

urlpatterns = [
    path("worker/", WorkerListAPI.as_view()),
    path("Careers/", CareerListAPI.as_view()),
    path("worker/<username>/", WorkerRetrieveUpdateAPI.as_view()),
]
