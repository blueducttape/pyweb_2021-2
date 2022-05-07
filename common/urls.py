from django.urls import path
from common import views
urlpatterns = [
path("hello/", views.HelloWorld.as_view()),
path("", views.IndexView.as_view()),

]
