from django.conf.urls import url
from member import views
# from django.urls import path

urlpatterns = [
    url(r'^register', views.members),
    url(r'^list', views.members),
    url(r'^login', views.login),
    url(r'^modify', views.member_modify),
    url(r'^delete', views.member),
    # path('delete/<slug:pk>', views.member),

]

'''
CBV 방식 (Class Based View)
from django.conf.urls import url
from .views import Members as members
from .views import Member as member
from django.urls import path, include
urlpatterns = [
    path('/register', members.as_view()),
    path('/<int:pk>/', member.as_view()),
]
'''

'''
   url('/login', Member.as_view()),
   url('/list', Member.as_view())
   '''