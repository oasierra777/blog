from django.urls import path

from apps.blog.views import BlogListView
from apps.blog.views import BlogListCategoryView
from apps.blog.views import PostDetailView
from apps.blog.views import SearchBlogView

urlpatterns = [
    path('', BlogListView.as_view()),
    path('category/<category_id>', BlogListCategoryView.as_view()),
    path('<post_slug>', PostDetailView.as_view()),
    path("search/<str:search_term>", SearchBlogView.as_view()),
]
