from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class register(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(password=make_password(request.data['password']))
            return Response("Register Successfull",
                            201)
        return Response(serializer.errors, 400)


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user_check = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response('User not exist', 404)
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user_check)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, 201)
        else:
            return Response("Invalid Password", 400)
