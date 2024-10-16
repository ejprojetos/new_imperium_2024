from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated # Or your permission logic 
from .models import User
from .serializers import UserWithRolesSerializer


class UserView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        serializer = UserWithRolesSerializer(user)
        return Response(serializer.data)