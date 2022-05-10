from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from projects.views import ArticleViewSet
from feedback.views import FeedbackViewSet
from calculation.views import FileViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'projects', ArticleViewSet, basename='projects')
routes.register(r'feedback', FeedbackViewSet, basename='feedback')

# USER
routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls
]
