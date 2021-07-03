from rest_framework.view import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer

class UserEndPoint(APIView):

    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)