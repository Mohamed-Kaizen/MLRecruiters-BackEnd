from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import City, Issue, IssueProgress, Offer, Review, SubCity


class CityHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class SubCityHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class IssueHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("title", "customer", "city", "sub_city", "is_open")
    search_fields = ("name", "description")
    list_filter = ("is_open", "city__name", "sub_city__name")


class IssueProgressHistoryAdmin(SimpleHistoryAdmin):
    list_display = (
        "issue",
        "customer",
        "worker",
        "is_done_by_customer",
        "is_done_by_worker",
    )


class OfferHistoryAdmin(SimpleHistoryAdmin):
    list_display = (
        "from_customer",
        "to_worker",
        "worker_has_read_it",
        "worker_has_accepted",
    )


class ReviewHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("issue", "customer", "rate")
    list_filter = ("rate",)


admin.site.register(City, CityHistoryAdmin)
admin.site.register(SubCity, SubCityHistoryAdmin)
admin.site.register(Issue, IssueHistoryAdmin)
admin.site.register(IssueProgress, IssueProgressHistoryAdmin)
admin.site.register(Offer, OfferHistoryAdmin)
admin.site.register(Review, ReviewHistoryAdmin)
