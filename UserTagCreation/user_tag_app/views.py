from turtle import update
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework import status, generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate,login


class OverViewList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset=User_Tag.objects
    def get(self, request,*args, **kwargs):
        self.queryset=self.queryset.all().count()
        api_urls = {"User Registration":"http://localhost:8000/user_registration",
                    "User Login":"http://localhost:8000/user_login",
                    "User Tag creation":"http://localhost:8000/tag_create",
                    "Single User Tag Detail":"http://localhost:8000/detail_user_tag_list/"+"pk",
                    "Update User Tag Detail":"http://localhost:8000/update_user_tag/"+"pk",
                    "Delete User Tag Detail":"http://localhost:8000/delete_user_tag/"+"pk",
                    "Tag List":"http://localhost:8000/tag_list",
                    "Single Tag Detail":"http://localhost:8000/detail_tag_list/"+"pk",

            }
        return Response({
            'status':"success",
            'response_code': "200",
            'snippet_count':self.queryset,
            "URLS":api_urls

        })



class Registration(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, **kwargs):
        try:
            data=request.data
            if data:
                username=data['username']
                email=data['email']

                password1=data['password']
                password2=data['conform_password']
                if password1==password2:
                    user_obj=CustomUser(username=username,email=email)
                    user_obj.set_password(password1)
                    refresh=RefreshToken.for_user(user_obj)
                    user_obj.save()
                    return Response({'status': 'success','user_id':user_obj.id, 'response_code': status.HTTP_201_CREATED,'refresh':str(refresh),'access':str(refresh.access_token)})
                else:
                    return Response({'status': 'failed', 'response_code': status.HTTP_401_UNAUTHORIZED,"message":"password is incorrect"})
            return Response({'status': 'failed', 'response_code': status.HTTP_204_NO_CONTENT})

        except Exception as e:
            message = str(e)
            return Response({'status': 'error', 'response_code': 500, "message": message})


class UserLogin(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def create(self, request, **kwargs):
        try:
            data=request.data
            email=data['email']
            password=data['password']
            user_obj=authenticate(password=password,email=email)
            if user_obj:
                refresh=RefreshToken.for_user(user_obj)
                login(request,user_obj)
                return Response({'status': 'success','user_id':user_obj.id,'refresh':str(refresh),'access':str(refresh.access_token),'response_code': status.HTTP_200_OK})

            else:
                return Response({'status': 'failed', 'response_code': status.HTTP_401_UNAUTHORIZED,"message":"invalid user"})
        except Exception as e:
            message = str(e)
            return Response({'status': 'error', 'response_code': 500, "message": message})



class TagCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserTagSerializer
    def create(self, request, **kwargs):
        try:
            data=request.data
            user_id=request.user.id
            if data and user_id:
                print(request.data)
                tag_id=Tag.objects.filter(title=data['title']).first()
                if not tag_id:
                    tag_obj=Tag.objects.create(title=data['title'])
                    print("tag_obj",tag_obj.pk)
                    User_Tag.objects.create(title_id=tag_obj.pk,user_id=user_id,content=data['content'])
                else:
                    User_Tag.objects.create(title_id=tag_id.pk,user_id=user_id,content=data['content'])
                return Response({'status': 'success', 'response_code': status.HTTP_200_OK, 'message':"User Tag created" })
            return Response({'status': 'failed', 'response_code': status.HTTP_204_NO_CONTENT})

        except Exception as e:
            message = str(e)
            return Response({'status': 'error', 'response_code': 500, "message": message})


class UserTagDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset=User_Tag
    serializer_class = DetailUserTagSerializer


class UpdateUserTag(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=User_Tag
    serializer_class = UpdateUserTagSerializer
    def patch(self, request, **kwargs):
        try:
            print(request.data)
            data=request.data
            user_obj=User_Tag.objects.filter(pk=kwargs['pk']).first()
            if data:
                if user_obj:
                    print(user_obj.user)
                    tag_obj=Tag.objects.filter(title=user_obj.title).update(title=data['title'])

                    cust_obj=CustomUser.objects.filter(email=user_obj.user).update(username=data['user'])
                    user_obj.content=data['content']
                    user_obj.save()

                return Response({'status': 'success', 'response_code': status.HTTP_200_OK, 'message':"User Tag updated" })

        except Exception as e:
            message = str(e)
            return Response({'status': 'error', 'response_code': 500, "message": message})

class DeleteUserTag(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=User_Tag
    serializer_class = DetailUserTagSerializer
    def get(self, request, **kwargs):
        try:
            usertag_obj = User_Tag.objects.all()
            serializer_data=DetailUserTagSerializer(usertag_obj,many=True)
            return Response({'status': 'success', 'response_code': status.HTTP_200_OK, 'data': serializer_data.data})
        except Exception as e:
            message = str(e)
            return Response({'status': 'error', 'response_code': 500, "message": message})




class TagList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Tag.objects
    serializer_class = TagSerializer
    pagination_class=PageNumberPagination

 
    def get(self, request,*args, **kwargs):
        self.queryset=self.queryset.all()
        
        response = super().get(request,*args,**kwargs)
        return Response({
            'status':"success",
            'response_code': "200",
            'data':response.data
        })


class TagDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Tag
    serializer_class = TagSerializer