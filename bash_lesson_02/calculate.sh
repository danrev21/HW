#!/bin/bash

sum=$(($1 + $2))
dif=$(($1 - $2))
pro=$(($1 * $2))
quo=$(($1 / $2))

echo "Sum: $sum"
echo "Product: $pro"
echo "Quotient: $quo"
echo "Difference: $dif"

