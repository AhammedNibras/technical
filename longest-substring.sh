#!/bin/bash

# function to find the length of the longest substring without repeating characters
length_of_longest_substring() {
    s="$1"
    len=${#s}
    max_length=0

    for ((i = 0; i < len; i++)); do
        char_set=""
        current_length=0

        for ((j = i; j < len; j++)); do
            char="${s:j:1}"
            if [[ ! "$char_set" =~ "$char" ]]; then
                char_set+="$char"
                ((current_length++))
            else
                break
            fi
        done

        if ((current_length > max_length)); then
            max_length=$current_length
        fi
    done

    echo "$max_length"
}

# to test the function 
s="abcabcbb"
echo $(length_of_longest_substring "$s")