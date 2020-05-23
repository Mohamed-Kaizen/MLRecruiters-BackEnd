from rest_framework import serializers

from .models import Issue


class IssueCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ("title", "description", "city", "sub_city", "is_open")


class IssueSerializer(serializers.Serializer):

    title = serializers.CharField(read_only=True)

    description = serializers.CharField(read_only=True)

    customer = serializers.StringRelatedField(read_only=True)

    city = serializers.StringRelatedField(read_only=True)

    sub_city = serializers.StringRelatedField(read_only=True)


class IssueListSerializer(serializers.Serializer):

    uuid = serializers.UUIDField(read_only=True)

    title = serializers.CharField(read_only=True)

    city = serializers.StringRelatedField(read_only=True)

    sub_city = serializers.StringRelatedField(read_only=True)


#
# class UserDetailsSerializer(serializers.Serializer):
#
#     email = serializers.EmailField(read_only=True)
#
#     username = serializers.CharField(read_only=True)
#
#     picture = serializers.ImageField(read_only=True)
#
#     is_active = serializers.BooleanField(read_only=True)
#
#     is_customer = serializers.BooleanField(read_only=True)
#
#     is_worker = serializers.BooleanField(read_only=True)
#
#
# class WorkerListSerializer(serializers.Serializer):
#
#     username = serializers.CharField(read_only=True)
#
#     picture = serializers.ImageField(read_only=True)
#
#     careers = serializers.StringRelatedField(many=True)
#
#
# class CareerListSerializer(serializers.Serializer):
#
#     name = serializers.CharField(read_only=True)
#
#
# class JWTSerializer(serializers.Serializer):
#
#     access_token = serializers.CharField(read_only=True)
#
#     refresh_token = serializers.CharField(read_only=True)
#
#     user = UserDetailsSerializer(read_only=True)
#
#
# class CareerSerializer(serializers.StringRelatedField):
#
#     class Meta:
#         required = False
#
#     def to_internal_value(self, data: str) -> int:
#
#         career, created = Career.objects.get_or_create(name=data.capitalize())
#
#         return career
#
#
# class CustomRegisterSerializer(RegisterSerializer):
#
#     picture = serializers.ImageField(required=False)
#
#     full_name = serializers.CharField(max_length=300)
#
#     phone_number = serializers.CharField(max_length=10, min_length=9)
#
#     user_type = serializers.ChoiceField(choices=["worker", "customer"])
#
#     careers = CareerSerializer(many=True)
#
#     def get_cleaned_data(self):
#         data_dict = super().get_cleaned_data()
#         data_dict["picture"] = self.validated_data.get("picture", "")
#         data_dict["full_name"] = self.validated_data.get("full_name", "")
#         data_dict["phone_number"] = self.validated_data.get("phone_number", "")
#         data_dict["user_type"] = self.validated_data.get("user_type", "")
#         data_dict["careers"] = self.validated_data.get("careers", "")
#
#         return data_dict
#
#
# class WorkerSerializer(serializers.ModelSerializer):
#
#     careers = CareerSerializer(many=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ("username", "email", "full_name", "phone_number", "picture", "careers")
