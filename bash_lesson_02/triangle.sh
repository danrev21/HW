#!/bin/bash

echo  "Value of triangle sides: $1 $2 $3"

if [[ ! $1 =~ ^[1-9][0-9]?$|^100$ ]] || [[ ! $2 =~ ^[1-9][0-9]?$|^100$ ]] || [[ ! $3 =~ ^[1-9][0-9]?$|^100$ ]];
   then echo "Wrong"; exit;
fi

if [[ $1 -ne $2 ]] && [[ $1 -ne $3 ]] && [[ $2 -ne $3 ]];
   then echo "SCALENE";
elif [[ $1 -eq $2 ]] && [[ $1 -eq $3 ]] && [[ $2 -eq $3 ]];
   then echo "EQUILATERAL";
   else echo "ISOSCELES";
fi
