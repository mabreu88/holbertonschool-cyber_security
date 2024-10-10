#!/bin/bash
echo -n "$1$random_value"| openssl sha512 > 3_hash.txt
