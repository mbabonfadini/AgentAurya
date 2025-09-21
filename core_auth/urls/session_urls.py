from django.urls import path
from core_auth.views.session_view import SessionLoginView


urlpatterns = [
    path("auth/login/", SessionLoginView.as_view()),
]