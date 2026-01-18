# Ejercicio E: Render - CI/CD Continuo

## Resumen
Se han configurado pipelines de CI/CD en GitHub Actions para despliegue continuo y automático en Render, con integración de pruebas y verificación post-deploy.

## Apartados Completados

### Intensificación Técnica (1-2)
✅ **Apartado 1**: Cambios necesarios para desplegar DECIDE en Render con CI/CD
- Workflow GitHub Actions: `.github/workflows/render-deploy.yml`
- Configuración local_settings: `decide/local_settings_render.py`
- Dependencias de producción: `requirements.txt` actualizado

✅ **Apartado 2**: Commit y push realizado
- Commit: `feat: configurar CI/CD para despliegue continuo en Render`

## Componentes Implementados

### 1. Workflow de GitHub Actions: `render-deploy.yml`

El workflow se ejecuta automáticamente en cada **push a main** e incluye:

#### Job: `build-and-deploy`
- **Environment**: Ubuntu latest
- **Tests**: 
  - Corre tests del módulo `voting` contra PostgreSQL
  - Ejecuta migraciones previas
  - Verifica que la aplicación funciona antes del deploy
- **Deploy**: 
  - Usa API de Render para disparar despliegue
  - Requiere secrets: `RENDER_SERVICE_ID` y `RENDER_API_KEY`

#### Job: `post-deploy`
- **Trigger**: Solo si `build-and-deploy` tiene éxito
- **Verificación**: 
  - Realiza health checks contra la API
  - Reintentos automáticos (hasta 30 intentos)
  - Confirma que el servicio está respondiendo

### 2. Configuración de Render: `local_settings_render.py`

Fichero de configuración específico para ambiente de producción:

```python
# Base de datos
- Detección automática via DATABASE_URL
- Pool de conexiones: 600 segundos
- Fallback a configuración local si no hay DATABASE_URL

# Seguridad (Producción)
- SECURE_SSL_REDIRECT = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- SECURE_PROXY_SSL_HEADER configurado

# Estáticos
- STATIC_ROOT: /staticfiles/
- Servidos por Render con collectstatic

# CORS
- Permitidos dominio de Render únicamente
```

### 3. Actualización de Dependencias

Nuevas dependencias añadidas a `requirements.txt`:

| Librería | Versión | Propósito |
|----------|---------|----------|
| `gunicorn` | 21.2.0 | WSGI server para Render |
| `whitenoise` | 6.6.0 | Servir archivos estáticos sin Nginx |
| `dj-database-url` | 1.3.0 | Parsear DATABASE_URL |
| `requests` | 2.31.0 | Health checks post-deploy |

### 4. Actualización de Settings

Modificación en `decide/settings.py`:

```python
# Detección automática del ambiente
if DATABASE_URL o ENVIRONMENT == 'render':
    Cargar local_settings_render.py
else:
    Cargar local_settings.py
```

## Flujo de CI/CD

```
Push a main
    ↓
[GitHub Actions: render-deploy.yml]
    ├─ Checkout código
    ├─ Setup Python 3.10.12
    ├─ Instalar dependencias
    ├─ Ejecutar tests (voting)
    │   ├─ Migrations
    │   └─ Tests unitarios
    ├─ Si tests pasan → Deploy en Render
    │   └─ Dispara API Render
    └─ Post-deploy checks
        ├─ Health check
        ├─ Reintentos automáticos
        └─ Confirmación de servicio
```

## Configuración Requerida en Render

Para que funcione el workflow, es necesario:

1. **Crear secrets en GitHub**:
   ```
   RENDER_SERVICE_ID: <ID del servicio en Render>
   RENDER_API_KEY: <API key de Render>
   ```

2. **Variables de entorno en Render**:
   ```
   DATABASE_URL: postgresql://usuario:contraseña@host:5432/decide
   BASEURL: https://decide-render.onrender.com
   DEBUG: False
   ENVIRONMENT: render
   ```

3. **Build Command** (en Render):
   ```bash
   pip install -r requirements.txt && cd decide && python manage.py migrate --noinput && python manage.py collectstatic --noinput
   ```

4. **Start Command** (en Render):
   ```bash
   cd decide && gunicorn decide.wsgi:application --bind 0.0.0.0:$PORT
   ```

## Verificación del Despliegue

Después de un push a main:

```bash
# Ver ejecución del workflow
gh run list --workflow render-deploy.yml

# Ver logs del despliegue
gh run view <run-id> --log

# Comprobar logs en Render
# https://dashboard.render.com/services/<service-id>/logs
```

## Ventajas de esta Implementación

✅ **Automatización completa**: Push → Test → Deploy  
✅ **Tests previos**: Verifica antes de desplegar  
✅ **Verificación post-deploy**: Comprueba salud del servicio  
✅ **Ambiente aislado**: Configuración específica para Render  
✅ **Rollback automático**: Render maneja reversiones en caso de error  
✅ **Transparencia**: Logs completos en GitHub Actions y Render  

## Notas Importantes

- El workflow requiere que Render esté previamente configurado con la base de datos
- Los secrets de GitHub deben estar configurados antes de ejecutar
- Las migraciones se ejecutan automáticamente en el post-deploy de Render
- Los archivos estáticos se sirven con WhiteNoise (sin necesidad de Nginx extra)
- La configuración de SSL es automática mediante Render
