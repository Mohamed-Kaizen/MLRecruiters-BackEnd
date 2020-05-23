from django_filters import rest_framework as filters

from .models import Issue


class IssueFilter(filters.FilterSet):
    class Meta:
        model = Issue
        fields = ("city", "sub_city")
