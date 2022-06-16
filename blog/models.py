import datetime
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.FileField(upload_to='blog/templates/posts/')
    is_featured = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)