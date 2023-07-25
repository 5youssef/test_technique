# Stage 1: Build the Vuetify Frontend

FROM node:16 AS frontend




# Set the working directory for the frontend

WORKDIR /app




# Copy the frontend code

COPY ./package*.json /app/

COPY ./ /app/




# Install dependencies and build the frontend

RUN npm set strict-ssl false

RUN npm install

RUN npm run build




# Stage 2: Production Image

FROM nginx:latest




# Remove the default Nginx static content

RUN rm -rf /usr/share/nginx/html/*




# Copy the built frontend from the frontend stage to the final image

COPY --from=frontend /app/dist /usr/share/nginx/html




# Expose the port on which your frontend will run (default: 80)

EXPOSE 3000




# Start Nginx to serve the frontend

CMD ["nginx", "-g", "daemon off;"]