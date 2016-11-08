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

# http://gs.statcounter.com/?PHPSESSID=5j5ugptrksqdb6pmquga0qspk7#resolution-ww-monthly-201507-201606
# iPhone 5, iPhone 6, iPhone 6 Plus, iPad, "standard laptop", "higher end laptop"
RESOLUTIONS="320x568 375x667 414x736 768x1024 1366x768 1920x1080"

for RES in $(echo ${RESOLUTIONS}); do
    WIDTH=$(echo ${RES} | awk -F 'x' '{print $1}')
    OUTFILE=$(echo ${INFILE} | sed "s/\./${WIDTH}\./")
    # Only Shrink Larger Images ('>' flag)
    convert ${INFILE} -resize "${RES}>" ${OUTFILE}
done
