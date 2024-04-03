from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class Roles(models.IntegerChoices):
    ADMIN = 0, "Administrador"
    PATIENT = 1, "Paciente"
    DOCTOR = 2, "Médico"
    NUTRITIONIST = 3, "Nutricionista"
    PSYCHOLOGIST = 4, "Psicólogo"
    PERSONAL_TRAINER = 5, "Personal Trainer"
    OTHERS = 6, "Outros"


class User(AbstractBaseUser, PermissionsMixin):   
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role = models.IntegerField(choices=Roles.choices, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
    
    def get_short_name(self):
        return self.first_name
