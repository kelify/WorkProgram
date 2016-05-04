#!/bin/bash

until [ -z "$1" ]
do 
echo -ne "$1\t"
shift
done 
echo 
exit 0
