#!/bin/bash
sudo nmap -p$2 -sW --exclude-ports $3 $1
