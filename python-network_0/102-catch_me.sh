#!/bin/bash
# makes a request to a file and gets a response message
curl -sLX PUT -d "user_id=98" -H "origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
