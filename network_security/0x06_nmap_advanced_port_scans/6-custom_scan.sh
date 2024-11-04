#!/bin/bash
sudo nmap -p$2 -sX $1 -oN custom_scan.txt &> /dev/null
