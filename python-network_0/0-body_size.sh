#!/bin/bash 
# take in a url and display the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
