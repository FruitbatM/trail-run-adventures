from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=75)
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.name
