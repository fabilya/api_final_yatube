from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


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
router.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
