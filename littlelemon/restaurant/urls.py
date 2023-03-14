from django.urls import path, include
from rest_framework import routers
from .views import MenuItemView, SingleMenuItemView

router = routers.DefaultRouter()
router.register(r'menu', MenuItemView)
urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', MenuItemView.as_view())
    # path('', include(router.urls))
]