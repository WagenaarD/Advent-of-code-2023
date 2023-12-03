#!/usr/bin/env bash
# source: https://github.com/Janiczek/advent-of-code/blob/master/start.sh#L8-L11
# explanation: https://www.reddit.com/r/adventofcode/comments/e32v5b/need_help_with_input_download_script_bash/
# 
# Requires the creation of a file in the _utils folder named aoc_session_cookei.sh containing the 
# AOC_SESSION_COOKIE variable.
# 
# Run like (for day 01 of 2023):
# sh ../_utils/get_input.sh

source ../_utils/aoc_session_cookie.sh

# Get the input parameters
YEAR=$(basename "$(dirname "$PWD")")
FOLDER_NAME=$(basename "$PWD")
DAY=${FOLDER_NAME:4} 
DAY_NO_ZEROS="$(echo $DAY | sed 's/^0*//')"

# Retreive the puzzle input
PUZZLE_URL="https://adventofcode.com/${YEAR}/day/${DAY_NO_ZEROS}/input"
PUZZLE_FILE="in"
curl "${PUZZLE_URL}" -H "cookie: session=${AOC_SESSION_COOKIE}" -o "${PUZZLE_FILE}" 2>/dev/null