#!/usr/bin/env bash

for f in {100..103}
do
    touch $f-script.js
    chmod u+x $f-script.js
done
