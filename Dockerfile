# Best Practice 1: Always pin a specific, secure, lightweight version. 
# Never just use 'nginx:latest'. We use 'nginx:1.25-alpine' for speed and safety.
FROM nginx:1.25-alpine

# Best Practice 2: Use LABEL to document ownership and maintainability.
LABEL maintainer="Luka Karchava"

# Take our new custom proxy rules and drop them into the settings vault
COPY nginx.conf /etc/nginx/nginx.conf

# Nginx alpine default configuration already handles 'daemon off;', 
# so we don't even need to override the CMD line anymore!
