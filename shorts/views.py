from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from shorts.models import Short, Like, Comment, Share
from user.models import User
from shorts.serializers import ShortSerializer, LikeSerializer, \
    CommentSerializer, ShareSerializer


class create_short(APIView):
    serializer_class = ShortSerializer

    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = ShortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)
    

class like_short(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, short_id):
        try:
            short = Short.objects.get(id=short_id)
        except Short.DoesNotExist:
            return Response('Short not found', 404)
        serializer = LikeSerializer(data=request.data)
        try:
            like = Like.objects.get(user=request.user, short=short)
            return Response('You have already liked this short', 208)
        except Like.DoesNotExist:
            if serializer.is_valid():
                serializer.save(user=request.user, short=short)
                return Response('Short liked successfully', 200)
            return Response(serializer.errors, 400)


class comment_on_short(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, short_id):
        try:
            short = Short.objects.get(id=short_id)
        except Short.DoesNotExist:
            return Response('Short not found', 404)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, short=short)
            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)


class share_short(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, short_id):
        try:
            short = Short.objects.get(id=short_id)
        except Short.DoesNotExist:
            return Response('Short not found', 404)
        serializer = ShareSerializer(data=request.data)
        try:
            send_to_user = User.objects.get(id=request.data['to_user'])
        except User.DoesNotExist:
            return Response('The user with you want to share is not exist')
        if serializer.is_valid():
            serializer.save(user=request.user, short=short)
            return Response({'Short shared successfully to user': request.data['to_user']}, 200)
        return Response(serializer.errors, 400)
