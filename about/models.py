from django.db import models


class Instructor(models.Model):
    """
    Instructor Profile Model
    """

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    about_content_1 = models.TextField(max_length=600)
    about_content_2 = models.TextField(max_length=600)
    image = models.ImageField(upload_to="instructors", null=True, blank=True)

    def __str__(self):
        return self.name
