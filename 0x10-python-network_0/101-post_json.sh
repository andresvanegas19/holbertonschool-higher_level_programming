#!/bin/bash
#  request with the contents of a file, passed with the filename
curl -s -H -d "Content-Type: application/json" -X POST @"$2" "$1"
