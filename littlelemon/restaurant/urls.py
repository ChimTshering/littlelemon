from django.urls import path, include
from rest_framework import routers
from .views import MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'menu', MenuItemView)
urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', MenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
    # path('', include(router.urls))
]