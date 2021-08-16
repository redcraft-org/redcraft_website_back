from django.urls import include, path
from api_v1.routers.ArticleRouter import ArticleRouter
from api_v1 import views


router = ArticleRouter()
router.register('article', views.ArticleViewSet, basename='article')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('<str:language>/', include(router.urls)),
]
