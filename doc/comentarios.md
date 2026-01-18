# Para este error: Error loading psycopg2 module: No module named 'psycopg2'
# añadir al requirements psycopg2-binary==2.9.8

# para el problema de "no module named pkg_resources"
# pip install setuptools

# Incompatibilidad django-nose con Python 3.10+
# Error: AttributeError: module 'collections' has no attribute 'Callable'
# Solución: Remover django-nose de requirements.txt y usar test runner nativo de Django
# Cambios:
#   - Removido: django-nose==1.4.7 de requirements.txt
#   - Removido: TEST_RUNNER = 'django_nose.NoseTestSuiteRunner' de settings.py
#   - Actualizado workflow: python manage.py test voting (runner nativo)

# CREACIÓN DE SUPERUSER PARA DOCKER
**Crear superusuario (si no existe):**
   ```bash
   docker exec -it decide_web ash
   cd /app/decide
   python manage.py shell
   ```
   
   Dentro del shell:
   ```python
   from django.contrib.auth.models import User
   User.objects.create_superuser('admin', 'admin@example.com', 'admin')
   print("Admin creado!")
   exit()
   ```