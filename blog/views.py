from argparse import Action
from rest_framework import viewsets,decorators
from rest_framework.views import APIView
from .models import Post, Like, Comment,Otp
from .serializers import PostSerializer, CommentSerializer, LikeSerializer,UserSerializer,OtpSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from rest_framework import status
from django.contrib.auth.models import User
from random import randint
from datetime import datetime, timedelta
from rest_framework_simplejwt import tokens


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,IsAdminUser)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    @action(detail=True)
    def comment(self,request,pk=None):
        post=self.get_object()
        print(post)
        comments=Comment.objects.filter(post=post)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
    @action(detail=True)
    def author(self,request,pk=None):
        post=self.get_object()
        print(post)
        user=User.objects.filter(post=post)
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

class OtpViewset(viewsets.ModelViewSet):
    queryset = Otp.objects.all()
    serializer_class = OtpSerializer
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        print(email)
        user = User.objects.get(email=email)
        print(user)
        if not user:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        otp = self.generate_otp()
        Otp.objects.create(user=user, otp=otp)

        # send_mail(
        #     'OTP Verification',
        #     f'Your OTP is {otp}',
        #     'surajraj506@gmail.com',
        #     [email],
        #     fail_silently=False,
        # )

        return Response({'message': 'OTP sent successfully.'}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        user = User.objects.get(email=email)
        print(user)
        if not user:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        otp_obj = self.get_otp(user, otp)
        print(otp_obj)
        if not otp_obj:
            return Response({'message': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)

        #otp_obj.delete()
        return Response({'message': 'OTP verified successfully.'}, status=status.HTTP_200_OK)

    def get_user(self, email):
        try:
            
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None

    def get_otp(self, user, otp):
        try:
            otp_obj = Otp.objects.get(user=user, otp=otp)
            print(otp_obj)
            otp_obj=OtpSerializer(otp_obj)
            print(otp_obj.data['created_at'])
            time_obj = datetime.strptime(otp_obj.data['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
            print(time_obj, type(time_obj))
            # formatted_time_str = time_obj.strftime('%Y-%m-%d %H:%M:%S.%f')
            #  = datetime.strptime(formatted_time_str, '%Y-%m-%d %H:%M:%S.%f')

            ex=time_obj+timedelta(minutes=5)
            print(datetime.now(), ex) 
        #print(otp_obj.data['created_at']+timedelta(minutes=5))
            print(type(datetime.now()), ex)    
            if(datetime.now()> ex):
                print("invalid")
                return None
            return otp_obj
        except Otp.DoesNotExist:
            return None

    def generate_otp(self):
        return str(randint(100000, 999999))

from django.shortcuts import render
from django.http import HttpResponse
#from .models import Item

from django.template.loader import render_to_string
def item_list(request):
    items =  User.objects.all()
    items={
        "items":items
    }
    print(items['items'])
    html_content = render_to_string("item.html",items)
    return HttpResponse(html_content)


class Login(APIView):
    def get(self, request):
        email = request.data.get('username')
        otp = request.data.get('password')
        user = User.objects.get(username=email)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate

class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Retrieve the username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Perform authentication
        user = authenticate(username=username, password=password)

        # If authentication fails, return an appropriate error response
        if not user:
            return Response({'error': 'Invalid username or password'}, status=401)

        # If authentication is successful, generate JWT tokens
        refresh = RefreshToken.for_user(user)

        # Return the generated tokens
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Your logic to fetch and process the data
        data = {
            'message': f'Hello, {user.username}! This is protected data.'
        }
        return Response(data)
