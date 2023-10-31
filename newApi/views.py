from rest_framework.decorators import api_view
from rest_framework.response import Response
from newApi.models import User  # Make sure you import the correct User model
# Correct the typo in 'serializers'
from newApi.serializers import userSerializer


@api_view()  # Specify the HTTP method you want to use
def user_list(request):
    users = User.objects.all()
    serializer = userSerializer(users, many=True)
    return Response(serializer.data)


@api_view()
def user_details(request, pk):
    user = User.objects.get(pk=pk)
    serializer = userSerializer(user)
    return Response(serializer.data)
