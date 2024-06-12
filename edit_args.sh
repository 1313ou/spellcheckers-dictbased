#!/bin/bash

source define_colors.sh
echo -e "${Z}"


DIR=.
if [[ ! $1 =~ [0-9]{8}-[nvars] ]]; then
  DIR="$1"
  shift
fi
echo "Target directory: $DIR"

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

for target in "$@"; do
  echo "${target}"
  r=$(grep -Hn "${target}" "${DIR}"/noun* "${DIR}"/verb* "${DIR}"/adj* "${DIR}"/adv*)
  if [ ! -z "${r}" ]; then
    f=$(echo "${r}" | awk -F  ':' '{print $1}')
    l=$(echo "${r}" | awk -F  ':' '{print $2}')
    echo -e "${G}${f} @ ${l}${Z}"
    wait_for_kate_sync --line ${l} "${f}"
  else
    echo -e "${R}${target}${Z}"
  fi

done

