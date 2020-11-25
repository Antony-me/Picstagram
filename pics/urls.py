from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import post_comment_create_and_list_view, like_unlike_post, PostUpdateView, PostDeleteView

app_name= 'pics'

urlpatterns=[
    path('', post_comment_create_and_list_view, name='main-post-view'),
    path('liked/', like_unlike_post, name='like-post-view'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<pk>/Delete/', PostDeleteView.as_view(), name='post-delete'), 
    # path(r'^search/', views.search_profile, name='search'),
]