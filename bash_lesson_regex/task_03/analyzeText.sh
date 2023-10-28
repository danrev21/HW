# Construct a script that accepts a given text input and 
# computes the occurrences of letters, digits, and specified 
# symbols, excluding any spaces.

# Guidelines:

# When provided with a string, the script should accurately tally:

# The number of alphabetic characters. 
# The number of numeric characters. 
# The quantity of special characters among [*!@#$%^&()_+]. 
# Whitespace or spaces should not be considered in these counts.

# ./analyzeText.sh "Hello1 &(*) 564gfhf"
# Digits: 4
# Special Characters: 4
# Alphabets: 9

#!/bin/bash

IFS=', ' read -a arr <<< $1

for i in ${arr[@]}; do
  if (( i % 2 == 0 )); then
    sum=$((sum + d))  
  fi
done
echo $sum
