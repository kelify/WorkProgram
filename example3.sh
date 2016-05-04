#!/bin/bash
#background-loop.sh
#前台程序优先于后台程序的先执行
for i in {1..10}
do
echo -n "$i"
done& 

echo 

for i in {11..20}
do 
echo -n "$i"
done 

echo

