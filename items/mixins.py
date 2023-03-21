from django.core.exceptions import PermissionDenied
class ItemOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        if item.seller != request.user:
            raise PermissionDenied("You are not the owner of this item")
        return super().dispatch(request, *args, **kwargs)