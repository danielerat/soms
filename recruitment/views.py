from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from recruitment.serializers import ApplySerializer
from recruitment.models import Application
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication


class ApplicationViewset(ModelViewSet):

    serializer_class = ApplySerializer
    queryset = Application.objects.all()

# Endpoint to receive applications from users.


class ApplyAPIView(APIView):
    authentication_classes = []

    def post(self, request):
        data = request.data
        serializer = ApplySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
