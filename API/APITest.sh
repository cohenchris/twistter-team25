#! /bin/bash

# This is a script that contains curl calls to test the Web Api

echo Create New User
curl -X POST \
-H "Content-Type: application/json" \
-d '{"username":"cornettn", "commonName":"Noah Cornett", "email":"blah", "description":"This is a desc"}' \
https://twistter-api.azurewebsites.net/user-create-new-user
printf "\n\n"

echo Update Common Name
curl -X POST \
-H "Content-Type: application/json" \
-d '{"userId":3, "newCommonName":"New Name"}' \
https://twistter-api.azurewebsites.net/user-update-common-name
printf "\n\n"

echo Invalid Json Test
curl -X POST \
-H "Content-Type: application/json" \
-d '{"invalid":3, "invalid":"New Name"}' \
https://twistter-api.azurewebsites.net/user-update-common-name
printf "\n\n"
