import os
from email.policy import default
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings

LORUM_IPSUM_LONG = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et tempor nisl. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices dolor."
LORUM_IPSUM_SHORT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et tempor nisl."

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    content_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'media/'))
    content = models.FileField(upload_to='blog/templates/posts/', storage=content_storage)
    preview = models.CharField(max_length=85, default=LORUM_IPSUM_SHORT)
    featured_preview = models.CharField(max_length=150, default=LORUM_IPSUM_LONG)
    is_featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnails/', default='thumbnails/default_image.png')
    tags = TaggableManager()
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
