# <アプリ名>/urls.py
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import BillViewSet, CreateUserView, UserViewSet

router = routers.DefaultRouter()
router.register('bills', BillViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('', include(router.urls)),
]
