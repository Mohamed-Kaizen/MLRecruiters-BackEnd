from typing import Dict, Tuple

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from loguru import logger
from rest_framework import exceptions, permissions, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_typed_views import typed_api_view

from . import filter, interfaces, models
from . import permissions as custom_permissions
from . import schema, serializers


class IssueViewSet(viewsets.ModelViewSet):

    queryset = models.Issue.objects.filter(is_open=True)

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_class = filter.IssueFilter

    search_fields = ("title", "description")

    ordering = ("title",)

    ordering_fields = ("city__name", "sub_city__name")

    lookup_field = "uuid"

    def get_serializer_class(self, *args: Tuple, **kwargs: Dict):

        if self.action == "create":
            return serializers.IssueCreateUpdateSerializer

        if self.action == "retrieve":
            return serializers.IssueSerializer

        if self.action == "update" or self.action == "partial_update":
            return serializers.IssueCreateUpdateSerializer

        return serializers.IssueListSerializer

    def get_permissions(self):

        if self.action == "create":

            permission_classes = (permissions.IsAuthenticated,)

        elif self.action == "update" or self.action == "partial_update":

            permission_classes = (
                permissions.IsAuthenticatedOrReadOnly,
                custom_permissions.IsOwnerOrReadOnly,
            )

        elif self.action == "destroy":

            permission_classes = (
                permissions.IsAuthenticatedOrReadOnly,
                custom_permissions.IsOwnerOrReadOnly,
            )

        else:

            permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        if self.request.user.is_customer:
            serializer.save(customer=self.request.user)
        else:
            raise exceptions.ValidationError(
                detail={"detail": "Your not customer"}, code=status.HTTP_400_BAD_REQUEST
            )


@swagger_auto_schema(
    method="post",
    operation_description="Send offer to worker",
    responses={
        400: "worker not found",
        401: "for non-customer users",
        201: "offer created",
    },
)
@typed_api_view(["POST"])
def create_offer(request: Request, offer: schema.CreateOffer):
    if request.user.is_customer and request.user.is_authenticated:
        try:
            user = interfaces.UserInterface().get_worker(username=offer.worker)

            models.Offer.objects.create(
                from_customer=request.user,
                to_worker=user,
                description=offer.description,
            )
            return Response(status=status.HTTP_201_CREATED)

        except Exception as error:
            logger.error(error)
            return Response(
                {"detail": "no such worker"}, status=status.HTTP_400_BAD_REQUEST
            )

    return Response(
        {"detail": "You can't do that"}, status=status.HTTP_401_UNAUTHORIZED
    )
