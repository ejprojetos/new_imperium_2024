from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied



class IsRoleUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado
        if request.user.is_anonymous:
            raise AuthenticationFailed(detail="User is not authenticated.", code="authentication_failed")
        
        required_roles = getattr(view, 'required_roles', [])
        user_roles = [role.name for role in request.user.roles.all()]
        #user_roles = getattr(request.user, 'roles', [])
        
        # Verifica se o usuário possui pelo menos um dos roles exigidos
        if not any(role in user_roles for role in required_roles):
            raise PermissionDenied(detail="User does not have the required role.", code="permission_denied")

        return True
