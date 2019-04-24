from django.urls import path, include
from . import views

app_name = 'blog'

"""

Below are the url patterns for the postlist view and post detail.
I am using url dispatcher from the django documentation.

"""

urlpatterns = [

   # path('', views.post_list, name='post_list'),
   path('', views.PostListView.as_view(), name='post_list'),
   path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]