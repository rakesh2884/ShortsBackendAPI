from rest_framework import serializers
from shorts.models import Short, Like, Comment, Share


class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Short
        fields = ['id',
                  'caption',
                  'content',
                  'user',
                  ]
        extra_kwargs = {'user': {'read_only': True}}


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id',
                  'short',
                  'user',
                  ]
        extra_kwargs = {'user': {'read_only': True},
                        'short': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id',
                  'comment',
                  'short',
                  'user',
                  ]
        extra_kwargs = {'user': {'read_only': True},
                        'short': {'read_only': True}}


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ['id',
                  'to_user',
                  'short',
                  'user',
                  ]
        extra_kwargs = {'user': {'read_only': True},
                        'short': {'read_only': True}}
