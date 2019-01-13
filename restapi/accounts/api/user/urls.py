from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token 
from .views import UserDetailAPIView,UserStatusAPIView

app_name = 'accounts'
urlpatterns = [
 
    path('<username>/',UserDetailAPIView.as_view()),
    path('<username>/status/',UserStatusAPIView.as_view())

]
