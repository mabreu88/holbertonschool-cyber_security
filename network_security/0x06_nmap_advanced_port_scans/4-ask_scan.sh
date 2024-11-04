#!/bin/bash
sudo nmap -p$2 -sA --reason --host-timeout 1000ms $1
