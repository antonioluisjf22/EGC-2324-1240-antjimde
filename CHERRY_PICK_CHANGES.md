# Cherry-Pick: Cambios de `egc_test` a `main`

## Resumen
Se trasladaron 3 commits específicos de la rama `egc_test` a la rama `main` utilizando `git cherry-pick`.

## Commits Aplicados

| Commit Original | Nuevo Hash | Mensaje | Cambios |
|---|---|---|---|
| `a76547b` | `1c6430b` | fix: fixed error | - Creación de `doc/comentarios.md` (5 líneas)<br>- Actualización de `requirements.txt` (+2 líneas) |
| `b28af22` | `22f5be6` | commit rq1 | - Modificación en `requirements.txt` (actualización de versión) |
| `196fc3c` | `3ff94c2` | commit rq2 | - Modificación en `requirements.txt` (actualización de versión) |

## Archivos Modificados

### `doc/comentarios.md`
- **Estado**: Archivo nuevo creado en el primer cherry-pick
- **Contenido**: 5 líneas añadidas

### `requirements.txt`
- **Cambios realizados**:
  1. `a76547b`: Agregadas 2 líneas (incluye `psycopg2-binary==2.9.8`)
  2. `b28af22`: Actualización de versión (cambio en línea)
  3. `196fc3c`: Actualización de versión (cambio en línea) - Resolvió conflicto con `selenium` (versión `4.7.1`)

## Resolución de Conflictos
Se encontró un conflicto en `requirements.txt` durante el tercer cherry-pick (`196fc3c`):
- **Conflicto**: Versión diferente de `selenium` (4.7.0 vs 4.7.1)
- **Resolución**: Se tomó la versión del cherry-pick (4.7.1)

## Estado Final
- **Rama**: `main`
- **Commits añadidos**: 3
- **Archivos afectados**: 2 (`doc/comentarios.md`, `requirements.txt`)

```bash
# Verificar cambios finales:
git log --oneline -5 main
# 3ff94c2 commit rq2
# 22f5be6 commit rq1
# 1c6430b fix: fixed error
# 2cbf63f enunciado
# 63f34d9 first commit
```
