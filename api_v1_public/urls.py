from django.urls import include, path
from api_v1_public.routers.BaseRouter import BaseRouter
from api_v1_public import views


router_article = BaseRouter()
router_article.register('article', views.ArticleViewSet, basename='article')

router = BaseRouter()
router.register('donation', views.DonationViewSet, basename='donation')
router.register('player', views.PlayerViewSet, basename='player')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('<str:language>/', include(router_article.urls)),
]
