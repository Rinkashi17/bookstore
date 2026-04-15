import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings') # Ajuste se o nome da sua pasta principal for outro
django.setup()

from django.contrib.auth.models import User

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    print(f"Criando superusuario: {username}")
    User.objects.create_superuser(username, email, password)
else:
    print("Superusuario ja existe.")