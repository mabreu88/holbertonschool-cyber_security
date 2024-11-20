#!/bin/bash
tail -n 1000 auth.log | awk '/Failed password/ {f[$NF]++} /Accepted password/ {s[$NF]++} END {for (u in s) if (f[u] && s[u]) print u}'

