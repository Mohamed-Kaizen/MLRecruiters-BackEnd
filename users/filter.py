from django_filters import rest_framework as filters

from .models import CustomUser


class WorkerFilter(filters.FilterSet):

    careers_name = filters.CharFilter("careers__name")

    class Meta:
        model = CustomUser
        fields = ("careers_name",)
