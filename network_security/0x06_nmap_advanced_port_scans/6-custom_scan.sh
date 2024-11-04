#!/bin/bash
sudo nmap -p$2 -sX --scanflags $1 -oN custom_scan.txt >/dev/null 2>&1
