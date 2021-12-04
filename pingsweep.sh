#!/usr/bin/bash

for ip in {1 .. 254} 
do 
    ping -c 1 l.l.l.$ip | grep "64 b" | cut -d " " -f 4 | tr -d ":" &
done