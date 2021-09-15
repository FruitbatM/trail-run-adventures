from django.db import models
from django.core.validators import MinLengthValidator


class BlogPost(models.Model):

    class Meta:
        ordering = ['-published_date']

    author = models.CharField(max_length=50, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # image will be uploaded to MEDIA_ROOT/blog
    header_image = models.ImageField(upload_to="blog", null=True, blank=True)
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=150, unique=True)
    intro_paragraph_1 = models.TextField(validators=[MinLengthValidator(100)],
                                         max_length=500)
    intro_paragraph_2 = models.TextField(validators=[MinLengthValidator(100)],
                                         max_length=500)
    subheading_1 = models.CharField(max_length=80)
    blog_content_1 = models.TextField(validators=[MinLengthValidator(250)])
    subheading_2 = models.CharField(max_length=80)
    blog_content_2 = models.TextField(validators=[MinLengthValidator(250)])
    blog_content_3 = models.TextField(validators=[MinLengthValidator(250)])
    # image will be uploaded to MEDIA_ROOT/blog
    blog_image_1 = models.ImageField(upload_to="blog", null=True, blank=True)
    subheading_3 = models.CharField(max_length=80)
    blog_content_4 = models.TextField(validators=[MinLengthValidator(250)])
    blog_content_5 = models.TextField(validators=[MinLengthValidator(250)])
    blog_content_6 = models.TextField(validators=[MinLengthValidator(250)])
    # image will be uploaded to MEDIA_ROOT/blog
    blog_image_2 = models.ImageField(upload_to="blog", null=True, blank=True)
    subheading_4 = models.CharField(max_length=55, null=True, blank=True)
    blog_content_7 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.author)
