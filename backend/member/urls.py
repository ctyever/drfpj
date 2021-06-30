from django.urls import path
from .views import Members, Member

urlpatterns = [
    path('/signup', Members.as_view()),
    path('/login', Member.as_view())
]