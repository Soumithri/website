# build stage
FROM node:12.6.0-alpine as build-stage
WORKDIR /app/
COPY frontend/package.json /app/
RUN npm cache verify
RUN npm install
COPY frontend /app/
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY nginx/prod.conf /etc/nginx/nginx.conf
COPY backend/static /usr/src/app/static/
COPY backend/media /usr/src/app/media/
COPY --from=build-stage /app/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]