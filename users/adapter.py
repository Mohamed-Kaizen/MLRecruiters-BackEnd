from allauth.account.adapter import DefaultAccountAdapter
from rest_framework import exceptions

from .validators import validate_reserved_name, validate_confusables_email, validate_confusables


class CustomAccountAdapter(DefaultAccountAdapter):

    def clean_username(self, username, shallow=False):

        username = super().clean_username(username, shallow)

        validate_reserved_name(
            value=username, exception_class=exceptions.ValidationError
        )

        validate_confusables(value=username, exception_class=exceptions.ValidationError)

        return username

    def clean_email(self, email):
        email = super().clean_email(email)
        local_part, domain = email.split("@")

        validate_reserved_name(
            value=local_part, exception_class=exceptions.ValidationError
        )

        validate_confusables_email(
            local_part=local_part,
            domain=domain,
            exception_class=exceptions.ValidationError,
        )

        return email

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)

        data = form.cleaned_data

        user.phone_number = data.get("phone_number")

        user.full_name = data.get("full_name")

        user.picture = data.get("picture")

        user.is_customer = True if data.get("user_type") == "customer" else False

        user.is_worker = True if data.get("user_type") == "worker" else False

        user.save()

        if data.get("user_type") == "worker":
            for career in data.get("careers"):
                user.careers.add(career)

        return user
