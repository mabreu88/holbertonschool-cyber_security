#!/bin/bash
ps -u "$1" -o pid,vsz,rss,comm --no-headers | awk '$2>0 && $3>0'
