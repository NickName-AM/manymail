from django.urls import path
from mail import views

urlpatterns = [
    path("", views.EmailSendAPIView.as_view(), name="email-send"),
]
