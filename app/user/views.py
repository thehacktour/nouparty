from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer

class UserEndPoint(APIView):

    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):

        data = {

            'name' : request.data.get('name'),
            'age' : request.data.get('age')

        }

        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)