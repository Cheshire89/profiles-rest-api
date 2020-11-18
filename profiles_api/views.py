from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):

    def get(self, request):
        return Response({'message':'HelloApiView', 'method': 'GET'})

    def post(self, request):
        return Response({'message': 'HelloApiView', 'method': 'POST'})

    def put(self, request, pk=None):
        return Response({'message':'HelloApiView', 'method': 'PUT', 'param': pk})

    def delete(self, request, pk=None):

        return Response({'message':'HelloApiView', 'method': 'DELETE', 'param': pk})


class HelloViewSet(ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        return Response({'message':'HelloViewSet', 'method': 'List'})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=self.data)
        if serializer.is_valid():
            name = serializer.validate_data().get('name')
            message = f'Hello {name}!'
            return Response({'message': message, 'method': 'Create'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID"""
        return Response({'message': 'HelloViewSet', 'method': 'retrieve', 'param': pk})

    def update(self, request, pk=None):
        """Handle updating an object by it's ID"""
        return Response({'message': 'HelloViewSet', 'method': 'update', 'param': pk})

    def partial_update(self, request, pk=None):
        """Handle partial update an object by it's ID"""
        return Response({'message': 'HelloViewSet', 'method': 'partial_update', 'param': pk})

    def destroy(self, request, pk=None):
        """Handle removing an object by it's ID"""
        return Response({'message': 'HelloViewSet', 'method': 'destroy', 'param': pk})