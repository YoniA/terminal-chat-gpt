#!/bin/bash

while true; do
    read -p "You: " input
    if [ "$input" == "exit" ]; then
        break
    fi
		echo -e "\n"		
		python query.py  "$input"
	
		echo -e "\n-----------------------"
done
