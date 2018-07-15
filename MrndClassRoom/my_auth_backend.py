from django.contrib.auth.backends import ModelBackend
from myAuth.models import Profile

class ProxiedModelBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None