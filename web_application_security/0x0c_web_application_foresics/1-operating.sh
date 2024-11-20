#!/bin/bash
grep "Linux version" dmesg | awk '{print "[    0.000000] "$0}'

