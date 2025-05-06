import os
import django
from django.utils import timezone

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/..")))

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imperium.settings')
django.setup()

from users.models import Role, User

def create_roles():
    roles = [
        {"name": "ADMIN", "description": "admin role"},
        {"name": "DOCTOR", "description": "doctor role"},
        {"name": "PATIENT", "description": "patient role"},
        {"name": "RECEPTIONIST", "description": "receptionist role"},
    ]
    for role_data in roles:
        role, created = Role.objects.get_or_create(name=role_data["name"], defaults={"description": role_data["description"]})
        if created:
            print(f"Role '{role.name}' criada.")
        else:
            print(f"Role '{role.name}' já existe.")

def create_admin_user():
    if User.objects.filter(email='admin@example.com').exists():
        print("Usuário admin já existe.")
        return

    admin_role = Role.objects.get(name="ADMIN")
    user = User.objects.create(
        email='admin@example.com',
        role=admin_role,
        cpf='00000000000',
        date_birth='1990-01-01',
        is_staff=True,
        is_superuser=True,
        is_active=True,
        date_joined=timezone.now()
    )
    user.set_password('admin123')
    user.save()
    print("Usuário admin criado com sucesso.")

if __name__ == "__main__":
    create_roles()
    create_admin_user()
