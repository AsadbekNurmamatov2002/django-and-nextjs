from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializirs import PostSerializers

# Create your views here.


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
    
posts_views_list=PostListApi.as_view()
