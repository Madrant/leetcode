#!/bin/bash

declare -a files=("file.txt")

loops=100

function exec_cmd_for_files()
{
    # Get name of a first parameter
    local name=$1[@]

    # Get first parameter as array by name
    local files=("${!name}")

    local cmd="${2}"

    echo "Command: '${cmd}'"

    for f in "${files[@]}"; do
        echo -e "\tFile: '${f}'"
        file_content=$(<"${f}")

        # Execute command
        eval $cmd <<< "${file_content}"

        # Profile command
        start_msec=$(date +%s%3N)

        for ((l=0; l<loops; l++)) do
            eval $cmd <<< "${file_content}" 2>&1 >/dev/null
        done

        stop_msec=$(date +%s%3N)

        step_msec=$((stop_msec - start_msec))

        echo -e "\t${loops} loops executed for: ${step_msec} msec"
        echo -e "\tStep time: $((step_msec/loops)) msec"
        echo -e "\n"
    done

    echo ""
}

# Show initial parameters
echo "Loops to profile: ${loops}"

echo "Files to test: ${#files[@]}"
for f in "${files[@]}"; do
    echo -e "\t${f}"
done
echo -e "\n"

# Test various commands
#
# awk
awk_script="transpose.awk"

# Convert multi-line awk script to one-line
awk_command=$(cat ${awk_script} | sed '/# /d' | tr '\n' ' ' | tr -s ' ')

cmd="awk '${awk_command}'"
exec_cmd_for_files files "${cmd}"

# rs
cmd="rs -c' ' -C' ' -T"
exec_cmd_for_files files "${cmd}"

exit 0
