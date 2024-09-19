#!/bin/bash

current_date=$(date +'%Y-%m-%d_%H:%M:%S')


git add .
git commit -m "Commit_$current_date"
git push -f
