from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from fabrica_needs.views import EntryViewSet, OutflowViewSet, ProductViewSet, WalletViewSet

router = DefaultRouter()
router.register(r"entries", EntryViewSet)
router.register(r"outflows", OutflowViewSet)
router.register(r"products", ProductViewSet)
router.register(r"wallet", WalletViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
