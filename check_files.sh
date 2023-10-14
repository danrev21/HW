#!/bin/bash

[ -f "data.txt" ] && echo "File data.txt found!"
[ -f "data.txt" ] || echo "File data.txt not found!"
cp data.txt backup.txt

