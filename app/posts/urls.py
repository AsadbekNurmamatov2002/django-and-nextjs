from django.urls import path 
from  .views import *

urlpatterns = [
    path("category/", category_view_list),
    path("", posts_views_list), 
]
