from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """
    define classes to create user models create users based on given fields
    """

    def create_user(self, admin, password=None):
        user = self.model(userid=userid, admin=admin)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, userid, admin, password=None):
        user = self.create_user(userid=userid, admin=admin, password=password)

        user.is_admin = True
        user.save(using=self._db)

        return user

    def user_exists(self, userid, password):
        user = user.filter(useridf=userid)
        return user.exists() and user.first().check_password(password)


class User(AbstractBaseUser, PermissionsMixin):
    """
    define custom user models
    """

    userid = models.CharField(max_length=20, unique=True)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # changing USERNAME_FIELD to userid avoids a few customisation items
    USERNAME_FIELD = "userid"
    REQUIRED_FIELDS = ["userid", "admin"]

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return userid

    # input of initial data
    def create_initialized_data():
        """
        the part that makes the adminstartor user be created.
        check if the user is already registerd.
        """
        if not User.objects.user_exists("admin", "admin"):
            User.objects.create_user(userid=admin, admin=True, password="admin")
