def is_admin(user):
    return user.is_superuser or user.is_staff


class RequestContextEmpty(Exception):
    pass


class Permission:
    def has_permission(self, user):
        return True

    def has_object_permission(self, user, obj):
        return True

    def check_permission(self, user, obj=None):
        perm = self.has_permission(user)
        if not perm:
            return False
        # Check object permission
        if obj:
            obj_perm = self.has_object_permission(user, obj)
            if not obj_perm:
                perm = obj_perm
        return perm


class IsAuthenticated(Permission):
    def has_permission(self, user):
        return user.is_authenticated


class IsAdmin(Permission):
    def has_permission(self, user):
        return is_admin(user)


class IsSuperadmin(Permission):
    def has_permission(self, user):
        return user.is_superuser


class PermissionMixin:

    permission_classes = []
    model_instance_name = "instance"

    def get_permission_classes(self):
        return self.permission_classes

    def get_permissions(self):
        permissions = [permission() for permission in self.get_permission_classes()]
        return permissions

    def has_permissions(self, user, obj=None):
        has_perm = True
        permissions = self.get_permissions()
        for permission in permissions:
            perm = permission.check_permission(user, obj)
            if not perm:
                has_perm = False
        return has_perm

    def is_shown(self, context=None):
        if context is None:
            raise RequestContextEmpty("Component permission need request context!")
        request = context["request"]
        instance = context.get(self.model_instance_name, None)
        user = request.user
        return self.has_permissions(user, instance)


class AuthenticatedMixin(PermissionMixin):

    permission_classes = [IsAuthenticated]


class AdminOnlyMixin(PermissionMixin):

    permission_classes = [IsAdmin]
