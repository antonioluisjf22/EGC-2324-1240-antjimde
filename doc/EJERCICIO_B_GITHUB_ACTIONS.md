# Ejercicio B: GitHub Actions - Workflows

## Resumen
Se han configurado dos workflows de GitHub Actions para automatizar pruebas y generar releases en el proyecto DECIDE.

## Apartados Completados

### Intensificación Colaborativa (1-4)
✅ **Apartado 1**: Workflow `django.yml` configurado para ejecutar pruebas **exclusivamente del módulo `voting`**
- Cambio: `./manage.py test` → `./manage.py test voting --keepdb`

✅ **Apartado 2**: Workflow preparado para ejecutarse **únicamente en cambios en `main`**
- Estructura: `on: push: branches: [main]`
- Se ejecuta en cada push a la rama principal

✅ **Apartado 3**: Cambios realizados, commitados y pusheados
- Commits incluyen correcciones en workflows

✅ **Apartado 4**: Verificación de funcionamiento
- Workflows se ejecutan correctamente en cada push a main

### Balance Técnico-Organizativo (5-7)
✅ **Apartado 5**: Workflow `django.yml` configurado con **dos versiones de Python**
- **Job `build-310`**: Pruebas con Python 3.10.12
- **Job `build-311`**: Pruebas con Python 3.11.6
- Ambos jobs ejecutan el módulo voting de forma independiente

✅ **Apartado 6**: Cambios realizados, commitados y pusheados
- Se corrigió versión incorrecta en job build-311 (estaba 3.10.12, ahora 3.11.6)
- Se renombraron jobs a `build-310` y `build-311` para cumplir validación YAML

✅ **Apartado 7**: Verificación de funcionamiento
- Ambos jobs se ejecutan en paralelo correctamente
- Cada versión de Python prueba el módulo voting

### Intensificación Técnica (8-10)
✅ **Apartado 8**: Workflow `release.yml` configurado para **generar releases automáticas**
- Se ejecuta en cada push a `main`
- Genera versión automáticamente: `v1.0.{número de commits}`
- Crea tag y release en el repositorio

✅ **Apartado 9**: Cambios realizados, commitados y pusheados
- Workflow `release.yml` incluido en repositorio

✅ **Apartado 10**: Releases creadas automáticamente
- Cada push a main genera una nueva release
- Versiones incrementales basadas en número de commits

## Archivos Modificados

### `.github/workflows/django.yml`
| Cambio | Descripción |
|--------|---|
| Indentación `on: push:` | Corregido para ejecutar solo en main |
| Jobs duplicados | Eliminada declaración duplicada de `jobs:` |
| Job `build-310` | Tests del módulo voting con Python 3.10.12 |
| Job `build-311` | Tests del módulo voting con Python 3.11.6 (versión corregida) |
| Nombres de jobs | Renombrados de `build-3.10/3.11` a `build-310/311` para validación YAML |
| Tests | Cambiados a `./manage.py test voting` |

### `.github/workflows/release.yml`
| Característica | Detalles |
|---|---|
| Trigger | `on: push: branches: [main]` |
| Versionado | Automático basado en commits |
| Release | Se crea en cada push a main |

## Flujo de Ejecución

```
Push a main
    ↓
[Dispara django.yml + release.yml en paralelo]
    ├─→ build-310 (Python 3.10.12)
    │   └─→ Test voting module
    ├─→ build-311 (Python 3.11.6)
    │   └─→ Test voting module
    └─→ release (crea automática release)
        └─→ Tag + Release creada
```

## Notas de Implementación

- **Nota**: Se utilizan dos jobs separados para Python en lugar de una matriz (matrix) por claridad y control individual, aunque computacionalmente no es óptimo.
- **Base de datos**: Se proporciona PostgreSQL 14.9 en ambos jobs para las pruebas.
- **Dependencias**: Se instalan `psycopg2` prerrequisitos necesarios para cada entorno.

## Verificación

Para verificar que todo funciona correctamente:

```bash
# Ver workflows en acción
git log --oneline | head -5
# Ver releases creadas
gh release list
# Ver acciones ejecutadas
gh run list --workflow django.yml
```
