from django import forms  
from blogapp.models import Blogs

class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Blogs  
        fields = "__all__"