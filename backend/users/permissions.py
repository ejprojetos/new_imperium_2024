from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Permissão baseada em papel. Verifica se o papel do usuário está
    na lista permitida para acessar a rota.
    """
    allowed_roles = []

    def has_permission(self, request, view):
        user_role = getattr(request.user, 'role', None)
        return user_role in self.allowed_roles
