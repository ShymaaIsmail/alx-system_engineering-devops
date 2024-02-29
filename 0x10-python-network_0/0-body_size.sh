#!/bin/bash
curl  -s  -w "%{size_header}\n" -o "/dev/null" "$1"
