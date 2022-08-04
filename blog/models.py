
from email.policy import default
import encodings
from encodings.utf_8 import encode
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.template.defaultfilters import slugify

LORUM_IPSUM_LONG = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et tempor nisl. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices dolor."
LORUM_IPSUM_SHORT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et tempor nisl."


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    pub_date = models.DateTimeField('date published')
    content = models.FileField(upload_to='blog/templates/posts/')
    preview = models.CharField(max_length=85, default=LORUM_IPSUM_SHORT)
    featured_preview = models.CharField(max_length=250, default=LORUM_IPSUM_LONG)
    is_featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnails/', default='thumbnails/default_image.png')
    tags = TaggableManager()
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         # Newly created object, so set slug
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)
