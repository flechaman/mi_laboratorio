# Instalacion: Windows 11 y WSL

## Objetivo

Preparar el equipo Windows 11 para trabajar con el laboratorio desde WSL.

## Requisitos

- Windows 11 actualizado.
- Permisos de administrador.
- Windows Terminal instalado.

## Pasos

Instalar WSL:

```powershell
wsl --install
```

Reiniciar si Windows lo solicita.

Actualizar WSL:

```powershell
wsl --update
wsl --status
```

Abrir la distribucion Linux y actualizar paquetes:

```bash
sudo apt update
sudo apt upgrade -y
```

Instalar utilidades base:

```bash
sudo apt install -y git curl tree make unzip ca-certificates
```

## Verificacion

```bash
wsl.exe --status
git --version
curl --version
tree --version
make --version
```

## Notas

- El laboratorio vive en `/mnt/e/Github/mi_laboratorio`.
- Windows Terminal debe usar el perfil de WSL para trabajar en el repo.
- Evita mezclar rutas Windows y Linux dentro de scripts del repo.
