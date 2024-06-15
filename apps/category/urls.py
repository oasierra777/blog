from django.urls import path

from apps.category.views import *

urlpatterns = [
    path('categories', ListCategoriesView.as_view()),
]
