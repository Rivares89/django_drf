from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, name, password=None, **extra_fields):
        """
        Create and return a superuser with the given email, name, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not name:
            raise ValueError('The Name field must be set')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
