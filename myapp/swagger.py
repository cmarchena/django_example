""" from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SwaggerSchemaView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Swagger API schema",
        responses={200: openapi.Response(description="Swagger API schema")},
    )
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
 """
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
)

urlpatterns = [
    # ...
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ...
]
