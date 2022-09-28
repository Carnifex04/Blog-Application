from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # corresponds to the UserList view
    path('users/', views.UserList.as_view()),
    # corresponds to the UserDetail view, using primary key(pk) as a keyword argument
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
