#!/bin/bash
echo -n $1 | sha1sum >> 0-hash.txt
