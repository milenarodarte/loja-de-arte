from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_employee = models.BooleanField(null=True, default=False)
    employee_passwod = models.CharField(null=True)
    email = models.CharField(max_length=127, unique=True)
    
    def __repr__(self) -> str:
        return f'<Recife ({self.id}) - {self.email} - {self.is_employee} - {self.username} - {self.first_name} - {self.last_name} - {self.birthdate}>'
# Create your models here.