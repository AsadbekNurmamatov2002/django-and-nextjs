from django.shortcuts import render
from rest_framework import generics
from .models import Post, Category, Tag
from .serializirs import PostSerializers, CategorySerializers, TagSerializers

# Create your views here.


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
    
posts_views_list=PostListApi.as_view()

class CategoryListApi(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers
    
category_view_list=CategoryListApi.as_view()


# Tag List Api Views
class TagViews(generics.ListAPIView):
    queryset=Tag.objects.all().order_by("?")
    serializer_class=TagSerializers

tag_view_list=TagViews.as_view()