from django.urls import path
from .views import list_view, detail_view, add_post

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
    path('add_post', add_post, name="add_post")
]
