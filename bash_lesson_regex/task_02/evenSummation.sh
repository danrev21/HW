# Receive an unordered set of numbers through a script. 
# Design a program to display the total of all even figures within this set.

# Instructions:
# Given an unarranged series of digits provided to the script, 
# the task is to compute and showcase the collective sum of numbers that are even.

# Sample Execution:
# ./evenSummation.sh "1,2,3,4,5,6,7"
# Displayed Output: 12

#!/bin/bash -v

#arr=$(echo $1 | sed 's/,/ /g')
#echo ${arr[@]}
#echo ${arr[2]}
#echo ${arr[@]:3:4}

IFS=', ' read -a arr <<< $1

for d in ${arr[@]}; do
  if (( d % 2 == 0 )); then
    sum=$((sum + d))  
  fi
done
echo $sum




