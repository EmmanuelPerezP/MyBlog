from django.forms import ModelForm
from .models import Post

class newPostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
            
