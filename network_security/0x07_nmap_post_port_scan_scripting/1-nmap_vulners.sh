#!/bin/bash
sudo nmap --script=vulners -p 80,443 $1
