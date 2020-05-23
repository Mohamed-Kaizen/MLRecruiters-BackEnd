"""users REST API URL Configuration"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "jobs"

router = DefaultRouter()

router.register("issues", views.IssueViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("offer/", views.create_offer),
]
