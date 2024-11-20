#!/bin/bash
grep "Linux version" dmesg | awk '{print $3}'

