from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Evreka API Documentation",
        default_version='v1',
        description="An API Documentation for Evreka Project",
        terms_of_service="https://www.evreka.co/tr",
        contact=openapi.Contact(email="bgunduz43@gmail.com"),
        license=openapi.License(name="Evreka License"),
    ),
    url='http://127.0.0.1:8000/swagger/',
    public=False
)