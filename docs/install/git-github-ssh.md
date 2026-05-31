# Instalacion: Git, GitHub y SSH

## Objetivo

Configurar Git para trabajar con GitHub sin pedir usuario y password en cada `push`.

## Configuracion basica

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@example.com"
git config --global init.defaultBranch master
```

## Crear clave SSH

```bash
ssh-keygen -t ed25519 -C "tu_email@example.com"
```

Acepta la ruta por defecto.

Mostrar clave publica:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copia la linea completa que empieza por `ssh-ed25519`.

## Alta en GitHub

En GitHub:

```text
Settings -> SSH and GPG keys -> New SSH key
```

Pega la clave publica y guarda.

## Probar conexion

```bash
ssh -T git@github.com
```

La primera vez responde `yes` para aceptar el host.

Salida esperada:

```text
Hi flechaman! You've successfully authenticated, but GitHub does not provide shell access.
```

## Cambiar remoto del repo a SSH

```bash
git remote set-url origin git@github.com:flechaman/mi_laboratorio.git
git remote -v
```

Debe mostrar:

```text
origin  git@github.com:flechaman/mi_laboratorio.git (fetch)
origin  git@github.com:flechaman/mi_laboratorio.git (push)
```

## Verificacion diaria

```bash
git status --short --branch
git push origin master
```

## Problemas habituales

- Si Git pide usuario/password, el remoto sigue en HTTPS.
- Si SSH falla con permisos, revisa que pegaste la clave publica `.pub`, no la privada.
- Si aparece host desconocido, ejecuta `ssh -T git@github.com` y acepta con `yes`.
