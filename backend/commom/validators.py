from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validar_email(email):
    try:
        validate_email(email)
        return email
    except ValidationError as e:
        return str(e)