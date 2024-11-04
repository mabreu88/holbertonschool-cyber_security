#!/bin/bash
sudo nmap -p 440-450 -sX --open --reason --packet-trace $1
