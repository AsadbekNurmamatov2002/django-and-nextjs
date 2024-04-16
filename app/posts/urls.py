from django.urls import path 
from  .views import *

urlpatterns = [
    path("", posts_views_list), 
    path("category/", category_view_list),
    # tag
    path("tag/", tag_view_list),
    path("tag/create/", tag_view_cerate),
    path("tag/<str:pk>/", tag_view_daital),
    
]
