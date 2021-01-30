from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    email = models.EmailField('E-Mail', max_length=200)
    phone = models.CharField('Phone Numbeer', max_length=14)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
