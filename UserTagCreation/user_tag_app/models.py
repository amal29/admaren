import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models



class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email,username,password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username,email, password, **extra_fields)

    def create_superuser(self,username, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,username, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null=True)


    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()


class Tag(models.Model):
    title = models.CharField(max_length=200, null=True,unique=True)
    def __str__(self):
        return f'{self.title}'
 

class User_Tag(models.Model):
  title=models.ForeignKey(Tag,related_name="tag_title", on_delete=models.CASCADE,null=True,blank=True)
  content = models.TextField(blank=True,null=True)
  user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
  timestamp=models.IntegerField(max_length = 200,default=datetime.datetime.now().timestamp())
  def __str__(self):
        return f'{self.title} of {self.user}'
