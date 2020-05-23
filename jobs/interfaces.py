from users.models import CustomUser


class UserInterface:
    @staticmethod
    def get_worker(*, username: str) -> CustomUser:
        return CustomUser.objects.get(username=username, is_worker=True)
