#!/bin/bash
sudo nmap -p 20,21,22,23,80,443 -sM -v $1 
