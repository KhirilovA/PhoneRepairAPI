from django.utils import timezone
from rest_framework import (viewsets,
                            mixins,
                            filters)
from rest_framework.permissions import AllowAny

from api.models import (User,
                        Request,
                        Invoice)
from api.serializers import (UserSerializer,
                             RequestDetailSerializer,
                             MasterRequestSerializer,
                             UserRequestSerializer,
                             InvoiceDetailSerializer,
                             MasterInvoiceSerializer,
                             UserInvoiceSerializer)
from api.permissions import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [AllowAny]

        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsMaster]

        return [permission() for permission in permission_classes]


class RequestCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RequestDetailSerializer
    queryset = Request.objects.none()
    permission_classes = [IsLoggedIn]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        user = User.objects.get(username=self.request.user)
        user.last_activity = timezone.now()
        user.save()


class RequestDetailViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'phone_model', 'description', 'status']

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MasterRequestSerializer
        else:
            return UserRequestSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Request.objects.all()
        else:
            return Request.objects.filter(user=self.request.user.id)

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsOwnerAndNotInProgress()]
        elif self.request.method in ['PUT', 'PATCH']:
            return [IsMasterOrNotInProgress()]
        return [IsOwnerOrMasterRequest()]


class InvoiceCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = InvoiceDetailSerializer
    queryset = Invoice.objects.none()
    permission_classes = [IsMaster]

    def perform_create(self, serializer):
        serializer.save()

        user = User.objects.get(username=self.request.user)
        user.last_activity = timezone.now()
        user.save()


class InvoiceDetailViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MasterInvoiceSerializer
        else:
            return UserInvoiceSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Invoice.objects.all()
        else:
            return Invoice.objects.filter(request__user=self.request.user.id)

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsMasterAndNotPaid()]
        elif self.request.method in ['PUT', 'PATCH']:
            return [IsMasterAndNotPaidOrOwner()]
        return [IsOwnerOrMasterInvoice()]
