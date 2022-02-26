# Keycloak RESTAPI cheatsheet by Ehsan Shirzadi

### Get token:
```
curl --location --request POST 'https://accounts.domain.com/auth/realms/master/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=admin-cli' \
--data-urlencode 'username=username' \
--data-urlencode 'password=password' \
--data-urlencode 'grant_type=password'```


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
