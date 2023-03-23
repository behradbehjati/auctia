from django.core.exceptions import PermissionDenied
class PaymentOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        payment = self.get_object()
        if payment.debtor != request.user:
            raise PermissionDenied("You dont have the access")
        return super().dispatch(request, *args, **kwargs)