from django.urls import (path,
                         include)
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views import (UserViewSet,
                       RequestCreateViewSet,
                       RequestDetailViewSet,
                       InvoiceCreateViewSet,
                       InvoiceDetailViewSet)


router = routers.DefaultRouter()
router.register(r'register', UserViewSet)
router.register(r'request', RequestCreateViewSet)
router.register(r'requests', RequestDetailViewSet, basename='requests')
router.register(r'invoice', InvoiceCreateViewSet),
router.register(r'invoices', InvoiceDetailViewSet, basename='invoices')

app_name = 'api'

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('', include((router.urls, 'api'))),
    path('docs/', schema_view)
]
