from users import views
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
# from users.views import CaptchaAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('captcha/', views.CaptchaAPIView.as_view()),
]
