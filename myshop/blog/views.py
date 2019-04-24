from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView

"""

I had a normal python function for the post list then changed to a class
which is a listview which allows to list any objects of any kind.

"""
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_list.html'


"""

In this view i have take the year month day and post parameters 
to retrieve a published post with the slug and date. Post has unique for date
in the slugfield, which will ensure one post will have one date to it.

"""

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   published__year=year,
                                   published__month=month,
                                   published__day=day)
    return render(request,'blog_detail.html',{'post': post})