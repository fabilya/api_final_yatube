from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from api.views import PostViewSet, CommentViewSet, GroupViewSet


app_name = 'api'

router = SimpleRouter()
router.register('posts',
                PostViewSet,
                basename='post'
                )
router.register('groups',
                GroupViewSet,
                )
router.register(r'^posts/(?P<id>\d+)/comments',
                CommentViewSet,
                basename='comment'
                )

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
