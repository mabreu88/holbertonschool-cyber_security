#!/bin/bash
sha256sum -c <(printf "%s %s\n" "$2" "$1")
