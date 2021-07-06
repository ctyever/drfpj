# from django.urls import path
# from .views import Boards as board
#
# urlpatterns = [
#     path('/register', board.as_view())
# ]

from django.conf.urls import url
from .views import Boards as board

urlpatterns = [
    url(r'^register', board.as_view()), #Class Based View 에서는 board.as_view() 형식으로 써야 됨

]