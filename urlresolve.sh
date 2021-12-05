#!/usr/bin/bash

for hostname in $(cat urls.txt);do
host $hostname | grep "has address" | cut -d " " -f 4 |sort -u &
done > urlips.txt

