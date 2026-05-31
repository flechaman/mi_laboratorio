# Instalacion: Starship

## Objetivo

Configurar un prompt informativo para ver directorio, rama Git y estado del repo.

## Instalar Starship

```bash
curl -sS https://starship.rs/install.sh | sh
```

Si requiere permisos:

```bash
curl -sS https://starship.rs/install.sh | sudo sh
```

Activar en Bash:

```bash
echo 'eval "$(starship init bash)"' >> ~/.bashrc
source ~/.bashrc
```

## Instalar fuente Nerd Font

Instala en Windows una fuente como:

```text
MesloLGS Nerd Font
```

En Windows Terminal:

```text
Settings -> Perfil WSL -> Appearance -> Font face
```

Selecciona `MesloLGS Nerd Font` o nombre equivalente.

## Configuracion

Archivo:

```bash
~/.config/starship.toml
```

El prompt debe mostrar:

- Ruta actual.
- Rama Git.
- Cambios sin trackear.
- Commits pendientes de push/pull.
- Hora.

## Verificacion

Entra en el repo:

```bash
cd /mnt/e/Github/mi_laboratorio
git status --short --branch
```

Si ves `?1`, hay un archivo sin trackear. Si ves `⇡1`, hay un commit pendiente de push.

## Problemas habituales

- Si ves simbolos raros, la fuente Nerd Font no esta seleccionada.
- Si Starship avisa de una clave desconocida, revisa `~/.config/starship.toml`.
- Si no cambia el prompt, revisa que `eval "$(starship init bash)"` esta en `~/.bashrc`.
