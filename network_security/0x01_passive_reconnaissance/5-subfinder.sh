#!/bin/bash
subfinder -d $1 -silent | while read d; do h=$(dig +short $d | grep '^[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}$' | head -n 1); echo $d,$h | tee -a $1.txt; done
