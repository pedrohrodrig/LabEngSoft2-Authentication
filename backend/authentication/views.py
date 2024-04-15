from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import (
    UserSerializer,
    UserBasicInfoSerializer
)
from .validators import (
    duplicated_email_validation,
    password_confirmation_validation
)

# Create your views here.
class UserView(ModelViewSet):
    queryset = User.objects.all()
    
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_data = serializer.validated_data
        user_data['password_confirmation'] = request.data['password_confirmation']

        duplicated_email_validation(user_data["email"])
        password_confirmation_validation(user_data["password"], user_data["password_confirmation"])

        user_data.pop("password_confirmation")

        user = User.objects.create_user(**user_data)
        user.set_password(user_data["password"])
        user.save()

        user_serialized = UserSerializer(user)

        return Response(user_serialized.data, status=status.HTTP_201_CREATED)
    
    def retrieve_self(self, request):
        user = User.objects.filter(id=request.user.id)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_basic_info_by_id(self, request, pk):
        user = User.objects.get(id=pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserBasicInfoSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request):
        active_users = User.objects.filter(is_active=True)

        serializer = UserBasicInfoSerializer(active_users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
