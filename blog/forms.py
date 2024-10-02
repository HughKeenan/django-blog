from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Allows authorised user to comment on a blog entry 
    post related to :model:`blog.Post`
    """
    class Meta:
        model = Comment
        fields = ('body',)