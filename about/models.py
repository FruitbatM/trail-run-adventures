from django.db import models


class Instructor(models.Model):
    """
    Instructor Profile Model
    """

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    about = models.TextField(max_length=900)
    image = models.ImageField(upload_to="instructors", null=True, blank=True)

    def __str__(self):
        return self.name
