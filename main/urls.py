from django.urls import path

from .views import ModelView

urlpatterns = [
    path('', ModelView.as_view(), name="home"),
]
