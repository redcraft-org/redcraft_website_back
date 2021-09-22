from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class BaseRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        DynamicRoute(
            url=r'^{prefix}/last/$',
            name='{basename}-last',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]
