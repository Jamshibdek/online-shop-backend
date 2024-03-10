from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schame_view = get_schema_view(
    openapi.Info(
        title="Product list Api",
        default_version= "v1",
        description="Product demo Project", 
        terms_of_service="demo.com",
        contact=openapi.Contact(email="jamshidbekwebdev@gmail.com"),
        license=openapi.License(name="Demo license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

router = SimpleRouter()
router.register("products", ProductViewset, basename="products")


urlpatterns = [
    path("products/", ProductListApiView.as_view()),
    path("products/create/", ProductCreateApiView.as_view()),
    path("product/", ProductListCreateApiView.as_view()),
    path("productupdatedelete/<int:pk>/", ProductUpdateDeleteView.as_view()),
    path("products/<int:pk>/", ProductDetailApiView.as_view()),
    path("products/<int:pk>/update/", ProductUpdateApiView.as_view()),
    path("products/<int:pk>/delete/", ProductDeleteApiView.as_view()),
    #swagger
    
    path("swagger/", schame_view.with_ui("swagger", cache_timeout=0), name="swagger-swagger-ui"),
    path("redoc/", schame_view.with_ui("redoc", cache_timeout=0), name="schame-redoc"),
          
]

urlpatterns = urlpatterns + router.urls