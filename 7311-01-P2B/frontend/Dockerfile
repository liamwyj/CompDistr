# Etapa 1: Construcción de la aplicación Vue.js
FROM node:18 AS build-stage

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia package.json y package-lock.json al contenedor
COPY package.json package-lock.json ./

# Instala las dependencias
RUN npm install

# Copia todo el código fuente al contenedor
COPY . ./

# Construye la aplicación Vue.js
RUN npm run build

# Etapa 2: Servir la aplicación con Nginx
FROM nginx:alpine AS production-stage

# Copia los archivos de la construcción al contenedor de Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expone el puerto 80
EXPOSE 80

# Comando por defecto para ejecutar Nginx
CMD ["nginx", "-g", "daemon off;"]
