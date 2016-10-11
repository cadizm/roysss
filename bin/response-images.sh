#!/bin/bash


CONVERT="$(which convert)"
if [[ -z ${CONVERT:-""} ]]; then
    echo "\`convert' missing, try \`brew install imagemagick'"
    exit 1
fi

INFILE=$1
if [[ -z ${INFILE:-""} ]]; then
    echo "Usage $0 <INFILE>"
    exit 1
fi

RESOLUTIONS="320x568 360x640 412x732 768x1024"

for RES in $(echo ${RESOLUTIONS}); do
    WIDTH=$(echo ${RES} | awk -F 'x' '{print $1}')
    OUTFILE=$(echo ${INFILE} | sed "s/\./${WIDTH}\./")
    # Only Shrink Larger Images ('>' flag)
    convert ${INFILE} -resize "${RES}>" ${OUTFILE}
done
