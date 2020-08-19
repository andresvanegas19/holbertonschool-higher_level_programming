#!/bin/bash
#  sends a POST request to the passed URL, and displays the body of the response
response="email: hr@holbertonschool.com
        subject: I will always be here for PLD"

curl -s -X POST --data "$response" "$1"
