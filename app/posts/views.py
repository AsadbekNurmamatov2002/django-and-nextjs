from django.shortcuts import render
from rest_framework import generics
from .models import Post, Category
from .serializirs import PostSerializers, CategorySerializers

# Create your views here.


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
    
posts_views_list=PostListApi.as_view()

class CategoryListApi(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers
    
category_view_list=CategoryListApi.as_view()