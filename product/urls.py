from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register("products", ProductViewset, basename="products")


urlpatterns = [
    # path("products/", ProductListApiView.as_view()),
    # path("products/create/", ProductCreateApiView.as_view()),
    # path("product/", ProductListCreateApiView.as_view()),
    # path("productupdatedelete/<int:pk>/", ProductUpdateDeleteView.as_view()),
    # path("products/<int:pk>/", ProductDetailApiView.as_view()),
    # path("products/<int:pk>/update/", ProductUpdateApiView.as_view()),
    # path("products/<int:pk>/delete/", ProductDeleteApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls