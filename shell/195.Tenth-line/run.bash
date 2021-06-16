#!/bin/bash

declare -a files=("less-than-ten.txt" "ten.txt" "more-than-ten.txt")

loops=1000

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
# gawk
cmd="gawk 'NR == 10'"
exec_cmd_for_files files "${cmd}"

# sed
cmd="sed '10!d'"
exec_cmd_for_files files "${cmd}"

# sed
cmd="sed -n '10p'"
exec_cmd_for_files files "${cmd}"

# tail + head
cmd="tail -n +10 | head -n 1"
exec_cmd_for_files files "${cmd}"

exit 0
