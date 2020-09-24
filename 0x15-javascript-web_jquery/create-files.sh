#!/usr/bin/env bash

for f in {1..10}
do
    touch $f-script.js
    chmod u+x $f-script.js
done
