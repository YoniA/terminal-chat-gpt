#!/bin/bash

readonly RED="$(tput setaf 1)" 
readonly GREEN="$(tput setaf 2)" 
readonly BLUE="$(tput setaf 4)" 
readonly BOLD="$(tput bold)" 
readonly BLINK="$(tput bold)" 
readonly RESET="$(tput sgr0)"


while true; do
    read -p "You: " input
    if [ "$input" == "exit" ]; then
        break
    fi

		echo -e "\n"		
		response=$(python client.py "$input")
		echo "${GREEN}$response${RESET}"
		echo -e "\n"
done
