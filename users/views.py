from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .models import CustomUser, Career
from .serializers import WorkerListSerializer, CareerListSerializer, WorkerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .filter import WorkerFilter
from .permissions import IsOwnerOrReadOnly


class WorkerListAPI(ListAPIView):
    queryset = CustomUser.objects.filter(is_worker=True)
    serializer_class = WorkerListSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_class = WorkerFilter

    search_fields = ("username", "full_name")

    ordering = ("username",)

    ordering_fields = ("careers__name", "username")


class WorkerRetrieveUpdateAPI(RetrieveUpdateAPIView):

    queryset = CustomUser.objects.filter(is_worker=True)

    serializer_class = WorkerSerializer

    permission_classes = (IsOwnerOrReadOnly, )

    lookup_field = "username"


class CareerListAPI(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerListSerializer
