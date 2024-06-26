from rest_framework import serializers
from .models import Post, Category, Tag
from django.contrib.auth.models import User


class UserSerailizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        

class PostSerializers(serializers.ModelSerializer):
    author=UserSerailizers(many=False, read_only=True)
    class Meta:
        model=Post
        fields=["id", 'title', 'category', 'body', 'author', 'publish', 'created', 'updated', 'status']
        depth = 1
        
    def validate(self, data):
        if data['title'] == data['body']:
            raise serializers.ValidationError('Invalid Title')
        return data

    def save(self, **kwargs):
        if self.instance:
            self.instance.title = self.validated_data['title']
            self.instance.body = self.validated_data['body']
            self.instance.author = self.validated_data['author']
            self.instance.publish = self.validated_data['publish']
            self.instance.created = self.validated_data['created']
            self.instance.updated = self.validated_data['updated']
            self.instance.status = self.validated_data['status']
            
            self.instance.save()

        else:
            self.instance = Post.objects.updated(**self.validated_data)
        return self.instance
    # def __init__(self, instance=None, *args, **kwargs):
    #     super(PostSerializers, self).__init__(instance, *args, **kwargs)
    #     self.Meta.depth=1


class CategorySerializers(serializers.ModelSerializer):
    post=PostSerializers(many=True, read_only=True)
    class Meta:
        model=Category
        fields=['name', 'post']
        depth = 1

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields= ["id",'tag', 'post']
        depth=2
    # def save(self, **kwargs):
        # if self.instance:
        #     self.instance.tag=self.validated_data['tag']
        #     self.instance.save()
        # else:
        #     self.instance=Tag.objects.update(**self.validated_data)
        # return self.instance
    def create(self, validated_data):
        # datas = validated_data.pop('post')
        tag = Tag.objects.create(**validated_data)
        # for data in datas:
            # Post.objects.create(tag=tag, **data)
        return tag
    
    def update(self, instance, validated_data):
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance