#!/bin/bash
res=$(grep "^smtpd_tls_security_level" /etc/postfix/main.cf | grep -w "may\|encrypt\|dane")
if [ -z "$res" ]; then
    echo "STARTTLS not configured"
fi
