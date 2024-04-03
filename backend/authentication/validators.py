from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


from .models import User

def duplicated_email_validation(email):
    users = User.objects.filter(email=email)

    if users.exists():
        raise ValidationError({"email": _("This email address is already registered for another user")})

def password_confirmation_validation(password, password_confirmation):
    if password and password_confirmation and password != password_confirmation:
        raise ValidationError({"password": _("Password and Confirmation must be identical")})
    
    try:
        password_validation.validate_password(password)
    except Exception as e:
        raise ValidationError({"password": e})