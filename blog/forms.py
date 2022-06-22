from django.forms import ModelForm
from .models import Post

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields= ['title', 'pub_date', 'content', 'is_featured', 'tags']
