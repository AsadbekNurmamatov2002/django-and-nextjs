from django.shortcuts import render
from rest_framework import generics
from .models import Post, Category, Tag
from .serializirs import PostSerializers, CategorySerializers, TagSerializers

# Create your views here.


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all().order_by("?")
    serializer_class=PostSerializers
    
posts_views_list=PostListApi.as_view()

class CategoryListApi(generics.ListAPIView):
    queryset=Category.objects.all().order_by("?")
    serializer_class=CategorySerializers
    
category_view_list=CategoryListApi.as_view()


# Tag List Api Views
class TagListAPi(generics.ListAPIView):
    queryset=Tag.objects.all().order_by("?")
    serializer_class=TagSerializers
    
tag_view_list=TagListAPi.as_view()

class TagCreateApi(generics.CreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializers
    
    def perform_create(self, serializer):
        # self.post=1
        print(serializer, "serialaizers")
        print(self, "self my tages")
        return super().perform_create(serializer)
    
tag_view_cerate=TagCreateApi.as_view()

class TagDaitalApi(generics.RetrieveAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializers
    lookup_field="pk"
    
tag_view_daital=TagDaitalApi.as_view()



