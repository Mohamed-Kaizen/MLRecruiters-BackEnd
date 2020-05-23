import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Rate(models.IntegerChoices):
    ONE = 1, _("One")
    TWO = 2, _("Two")
    THREE = 3, _("Three")
    FOUR = 4, _("Four")
    FIVE = 5, _("Five")


class City(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cites")

    def __str__(self) -> str:
        return f"{self.name}"


class SubCity(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("sub city")
        verbose_name_plural = _("sub cites")

    def __str__(self) -> str:
        return f"{self.name}"


class Issue(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    title = models.CharField(verbose_name=_("title"), max_length=255)

    description = models.TextField(verbose_name=_("description"))

    customer = models.ForeignKey(
        verbose_name=_("customer"),
        to=settings.AUTH_USER_MODEL,
        related_name="issues",
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_customer": True},
    )

    city = models.ForeignKey(
        verbose_name=_("city"), to=City, related_name="issues", on_delete=models.CASCADE
    )

    sub_city = models.ForeignKey(
        verbose_name=_("sub city"),
        to=SubCity,
        related_name="issues",
        on_delete=models.CASCADE,
    )

    is_open = models.BooleanField(verbose_name=_("is open"), default=True)

    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.title}"


class IssueProgress(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    customer = models.ForeignKey(
        verbose_name=_("customer"),
        to=settings.AUTH_USER_MODEL,
        related_name="customer_issue_progress",
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_customer": True},
    )

    worker = models.ForeignKey(
        verbose_name=_("worker"),
        to=settings.AUTH_USER_MODEL,
        related_name="worker_issue_progress",
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_worker": True},
    )

    issue = models.ForeignKey(
        verbose_name=_("issue"),
        to=Issue,
        related_name="issue_progress",
        on_delete=models.CASCADE,
        db_index=True,
    )

    is_done_by_customer = models.BooleanField(
        verbose_name=_("is done by customer"), default=False
    )

    is_done_by_worker = models.BooleanField(
        verbose_name=_("is done by worker"), default=False
    )

    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.issue} Progress"


class Offer(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    from_customer = models.ForeignKey(
        verbose_name=_("from customer"),
        to=settings.AUTH_USER_MODEL,
        related_name="customer_offer",
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_customer": True},
    )

    to_worker = models.ForeignKey(
        verbose_name=_("to worker"),
        to=settings.AUTH_USER_MODEL,
        related_name="worker_offer",
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_worker": True},
    )

    description = models.TextField(verbose_name=_("description"))

    worker_has_read_it = models.BooleanField(
        verbose_name=_("worker_has_read_it"), default=False
    )

    worker_has_accepted = models.BooleanField(
        verbose_name=_("worker has accepted"), null=True, default=None
    )

    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"Offer from {self.from_customer} to {self.to_worker}"


class Review(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    issue = models.ForeignKey(
        verbose_name=_("issue"),
        to=Issue,
        related_name="reviews",
        on_delete=models.CASCADE,
        db_index=True,
    )
    customer = models.ForeignKey(
        verbose_name=_("customer"),
        to=settings.AUTH_USER_MODEL,
        related_name="reviews",
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_customer": True},
    )

    rate = models.PositiveIntegerField(verbose_name=_("rate"), choices=Rate.choices)

    review = models.TextField(verbose_name=_("review"))

    history = HistoricalRecords()

    class Meta:

        verbose_name = _("review")

        verbose_name_plural = _("reviews")

    def __str__(self):
        return f"{self.rate} for {self.issue} by {self.customer}"
