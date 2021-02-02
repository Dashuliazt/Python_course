from django.db import models


# Create your models here.
class Customers(models.Model):
    """
    Model representing an users.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    profession = models.ForeignKey('Professions', on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.first_name} {self.second_nmae}'


class Professions(models.Model):
    profession_name = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.profession_name}'