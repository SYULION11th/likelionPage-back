from django.urls import path, include
from .views import QuestViewSet, QCommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', QuestViewSet)
router.register('qcomment', QCommentViewSet)

urlpatterns =[
    path('', include(router.urls)),
    # path('<int:quest_pk>/qcomment/', QCommentViewSet.as_view({'get': 'list', 'post':'create'})),
    path('user/', include('accounts.urls')),
]