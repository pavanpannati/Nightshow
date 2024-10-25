from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class LoginBackend(ModelBackend):
    def authenticate(email=None,password=None):
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None