from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class BlogPost(models.Model):

    class Meta:
        ordering = ['-published_date']

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True, blank=True, related_name='blog_posts')
    published_date = models.DateTimeField(auto_now_add=True)
    # image will be uploaded to MEDIA_ROOT/blog
    header_image = models.ImageField(upload_to="blog", null=True, blank=True)
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=150, unique=True)
    intro_paragraph_1 = models.TextField(validators=[MinLengthValidator(100)],
                                         max_length=500)
    intro_paragraph_2 = models.TextField(validators=[MinLengthValidator(100)],
                                         max_length=500, null=True, blank=True)
    subheading_1 = models.CharField(max_length=80, null=True, blank=True)
    blog_content_1 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)
    subheading_2 = models.CharField(max_length=80, null=True, blank=True)
    blog_content_2 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)
    blog_content_3 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)
    # image will be uploaded to MEDIA_ROOT/blog
    blog_image_1 = models.ImageField(upload_to="blog", null=True, blank=True)
    subheading_3 = models.CharField(max_length=70, null=True, blank=True)
    blog_content_4 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)
    blog_content_5 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)
    blog_content_6 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)
    # image will be uploaded to MEDIA_ROOT/blog
    blog_image_2 = models.ImageField(upload_to="blog", null=True, blank=True)
    subheading_4 = models.CharField(max_length=55, null=True, blank=True)
    blog_content_7 = models.TextField(validators=[MinLengthValidator(250)],
                                      null=True, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
