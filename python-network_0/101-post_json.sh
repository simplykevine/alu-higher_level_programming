#!/bin/bash
<<<<<<< HEAD
# sends a json POST request to a url
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2" 
=======
# Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
>>>>>>> 009d834382a5d75470e05567fcedd99abdfaa3dc
