from django.test import TestCase
from .forms import CommentForm
from .models import Post, User



#class TestCommentForm(TestCase):

#    def setUp(self):
#        self.user=User.objects.create_user(username='test',password='123')

#        self.post=Post.objects.create(
#            title='test',
#            slug='test', 
#            author=self.user,
#            content='test content'
#        )

#    def test_form_is_valid(self):
#        comment_form = CommentForm({'body': 'This is a great post'})
#        self.assertTrue(comment_form.is_valid())

#    def test_form_is_invalid(self):
#        comment_form = CommentForm({'body': ''})
#        self.assertTrue(comment_form.is_invalid(), msg='Form is not valid')    