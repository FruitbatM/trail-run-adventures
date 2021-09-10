from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    about = models.TextField(max_length=700)

    def __str__(self):
        return self.name
