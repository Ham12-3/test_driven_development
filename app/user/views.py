"""
Views for the user API

"""

from rest_framework import generics, status, authentication, permissions
from rest_framework.response import Response


from user.serializers import (UserSerializer,
                              EmailValidationSerializer,
                              AuthTokenSerializer)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class EmailValidationView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer_class = EmailValidationSerializer(data=request.data)
        if serializer_class.is_valid():
            # Your email validation logic here
            # You can check if the email already exists in your database, etc.
            return Response({'detail': 'Email is valid'}, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
