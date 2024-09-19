#!/bin/bash

current_date=$(date +'%Y-%m-%d_%H:%M:%S')

git config --get-all user.name PauloGomesNatixis
git config --get-all user.email paulo.gomes@natixis.com

git add .
git commit -m "Commit_$current_date"
git push -f
