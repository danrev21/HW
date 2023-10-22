#!/bin/bash

# Matching arguments to regex positive integer between 1 and 100:
for arg in $@
  do  	
    if [[ ! $arg =~ ^[1-9][0-9]?$|^100$ ]]; then
      echo "Input is wrong. Only positive integer between 1 and 100. Restart script."; exit
    fi
  done 

# or this way:
#if [[ ! $1 =~ ^[1-9][0-9]?$|^100$ ]] || [[ ! $2 =~ ^[1-9][0-9]?$|^100$ ]] || [[ ! $3 =~ ^[1-9][0-9]?$|^100$ ]];
#   then echo "Input is wrong. Restart script."; exit;
#fi

# Checking triangle type:
if [[ $1 -ne $2 ]] && [[ $1 -ne $3 ]] && [[ $2 -ne $3 ]];
   then echo "SCALENE";
elif [[ $1 -eq $2 ]] && [[ $1 -eq $3 ]] && [[ $2 -eq $3 ]];
   then echo "EQUILATERAL";
   else echo "ISOSCELES";
fi
