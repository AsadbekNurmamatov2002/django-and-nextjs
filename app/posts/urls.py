from django.urls import path 
from  .views import *

urlpatterns = [
    path("", posts_views_list), 
    path("category/", category_view_list),
    path("tag/", tag_view_list),
]
