from rest_framework import routers

from residential.api import views

router = routers.DefaultRouter()

router.register(r'residence', views.ResidenceViewSet)
router.register(r'package', views.PackageViewSet)

urlpatterns = router.urls
