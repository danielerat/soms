from rest_framework.views import APIView
from rest_framework.response import Response
from recruitment.serializers import ApplySerializer
# Endpoint to receive applications from users.


class ApplyAPIView(APIView):
    authentication_classes = []

    def post(self, request):
        data = request.data
        serializer = ApplySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
