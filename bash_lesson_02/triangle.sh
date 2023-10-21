#!/bin/bash

echo  "Value : $1"

if [[ ! $1 =~ ^[1-9][0-9]?$|^100$ ]] ;
   then echo "Wrong";
fi


