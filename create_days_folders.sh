#!/bin/bash

for i in {01..25}; do
    mkdir -p "day-$i/python"
    touch "day-$i/python/solution.py"
    echo "import os" > "day-$i/python/solution.py"
done

