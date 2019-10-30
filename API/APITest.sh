#! /bin/bash

# This is a script that contains curl calls to test the Web Api

echo Create New User
curl -X POST \
-H "Content-Type: application/json" \
-d '{"username":"cornettn", "commonName":"Noah Cornett", "email":"blah", "phone":"2197793959", "birthday":"00/00/0000", "description":"This is a desc"}' \
localhost:5000/user-create-new-user
printf "\n\n"

echo Update Common Name
curl -X POST \
-H "Content-Type: application/json" \
-d '{"userId":3, "newCommonName":"New Name"}' \
localhost:5000/user-update-common-name
printf "\n\n"

echo Update Phone Number
curl -X POST \
-H "Content-Type: application/json" \
-d '{"userId":3, "newPhoneNumber":"(219) 779-3959"}' \
localhost:5000/user-update-phone
