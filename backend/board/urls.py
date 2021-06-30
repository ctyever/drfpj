from django.urls import path
from .views import Boards as board

urlpatterns = [
    path('/postup', board.as_view())
]