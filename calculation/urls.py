from django.urls import path
from .views import FileViewSet
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', FileViewSet.as_view()),
    path('articles/<int:pk>', FileViewSet.as_view())
]