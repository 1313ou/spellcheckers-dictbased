#!/bin/bash

source define_colors.sh
echo -e "${Z}"

FILE=diffs
FILE=.
if [ ! -z "$1" ]; then
  FILE="$1"
fi


DIR=.
if [ ! -z "$2" ]; then
  DIR="$2"
fi

function wait_for_kate_async() {
  kate "$@" &
  pid=$! # or $(jobs -p)
  wait ${pid}
}

function wait_for_kate_sync() {
  kate "$@"
  while pgrep -x "kate" > /dev/null; do
    sleep 1
  done
}


while read line; do
  #echo "$line"
  target=$(echo "${line}" | awk '{print $1}')
  if [ -z "${target}" ]; then
    continue
  fi
  echo -e "${Y}${target}${Z}"
  r=$(grep -Hn "${target}" "${DIR}"/noun* "${DIR}"/verb* "${DIR}"/adj* "${DIR}"/adv*)
  echo -e "${B}${r}${Z}"
  f=$(echo "${r}" | awk -F  ':' '{print $1}')
  l=$(echo "${r}" | awk -F  ':' '{print $2}')
  echo -e "${G}${f} @ ${l}${Z}"
  
  wait_for_kate_sync --line ${l} "${f}" 
  
done < "${FILE}"

