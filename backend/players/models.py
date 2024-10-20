from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
