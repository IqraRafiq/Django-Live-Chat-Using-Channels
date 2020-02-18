from django.urls import path, include
# from django.contrib.auth import views as 

from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter(trailing_slash=False)

router.register('profile', views.UserProfileViewSet)



urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
  