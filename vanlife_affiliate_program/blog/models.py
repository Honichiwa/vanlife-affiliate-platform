from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    blog_slug = models.SlugField("Blog slug", null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.blog_slug

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ['-published']