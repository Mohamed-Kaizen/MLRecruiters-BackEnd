import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


def user_upload_to(instance: "CustomUser", filename: str):

    return f"images/profile_pics/{instance.username}/{filename}"


class Career(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("career")
        verbose_name_plural = _("careers")

    def __str__(self) -> str:
        return f"{self.name}"


class CustomUser(AbstractUser):

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    full_name = models.CharField(verbose_name=_("full name"), max_length=300)

    phone_number = models.CharField(
        verbose_name=_("phone number"), max_length=10, unique=True
    )

    picture = models.ImageField(
        verbose_name=_("picture"),
        default="images/default/pic.png",
        upload_to=user_upload_to,
    )

    careers = models.ManyToManyField(
        verbose_name=_("careers"), to=Career, related_name="workers", blank=True
    )

    is_customer = models.BooleanField(
        verbose_name=_("is customer"), null=True, blank=True
    )

    is_worker = models.BooleanField(verbose_name=_("is worker"), null=True, blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self) -> str:
        return f"{self.username}"
