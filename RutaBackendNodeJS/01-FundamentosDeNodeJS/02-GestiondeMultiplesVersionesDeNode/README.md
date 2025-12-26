# Instalación y uso de NVM (Node Version Manager)

Este documento explica cómo instalar **NVM**, verificar su instalación,
listar versiones disponibles e instalar/cambiar versiones de
**Node.js**.

------------------------------------------------------------------------

## 🚀 Instalación de NVM

1.  Visita el siguiente enlace para más información:\
    👉 https://nodejs.org/es/download

2.  Ejecuta el siguiente comando para instalar NVM:

``` bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

3.  Carga NVM en tu sesión actual:

``` bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # Carga nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # Autocompletado
```

4.  Actualiza tu terminal:

``` bash
source ~/.zshrc
```

------------------------------------------------------------------------

## ✔️ Verificar instalación

``` bash
nvm --version
nvm -v
```

------------------------------------------------------------------------

## 📋 Listar versiones disponibles

``` bash
nvm ls
```

------------------------------------------------------------------------

## 📦 Instalar Node.js

Ejemplo instalando la versión **24**:

``` bash
nvm install 24
```

------------------------------------------------------------------------

## 🔄 Cambiar de versión de Node.js

Ejemplo para usar la versión **23**:

``` bash
nvm use 23
```
