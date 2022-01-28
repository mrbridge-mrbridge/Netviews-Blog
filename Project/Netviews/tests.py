from django.test import TestCase
from .models import Post
from django.views import Generic
# Create your tests here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    

class DetailView(generic.Detailview):
    model = Post
    template_name = 'post_detail.html'