def role_factory():
    from users.models import Role

    roles = [
        {
            'name': 'ADMIN',
            'description': 'Admin'
        },
        {
            'name': 'PATIENT',
            'description': 'Paciente'
        },
        {
            'name': 'DOCTOR',
            'description': 'Médico'
        },
        {
            'name': 'RECEPTIONIST',
            'description': 'Recepicionista'
        },
    ]

    for role in roles:
        Role.objects.get_or_create(name=role['name'], defaults={
            'description': role['description']
        })


role_factory()
