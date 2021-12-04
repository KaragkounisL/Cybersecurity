#!/usr/bin/bash

for ip in $(cat ips.txt); do nmap -sV -sC -Pn $ip &
done > nmaps.txt
