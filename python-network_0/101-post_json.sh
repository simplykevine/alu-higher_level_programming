#!/bin/bash
# sends a json POST request to a url
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2" 
