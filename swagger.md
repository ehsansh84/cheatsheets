# Swagger cheatsheet by Ehsan Shirzadi

### Swagger-ui for your documentation:
Put your docs in a file named `swagger.yaml`
then create this Dockerfile beside that:
```yaml
version: '3.3'
services:
  swagger-ui:
    container_name: cman-swagger
    image: swaggerapi/swagger-ui
    restart: unless-stopped
    ports:
            - 8001:8080
    environment:
      SWAGGER_JSON: /swagger.yaml
    volumes:
      - ${PWD}/swagger.yaml:/swagger.yaml
```
That's it! now you can see your docs on `localhost:8001`

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
