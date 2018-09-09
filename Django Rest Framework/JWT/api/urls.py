from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserViewset

router = SimpleRouter()
router.register('users' , UserViewset , base_name='users')

urlpatterns = router.urls + [url(r'^get_jwt_token' , obtain_jwt_token , name = "get_jwt_token")]
