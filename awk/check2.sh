#!/bin/bash

awk 'BEGIN	{ RS="";FS="\n"}
     /(^|\n)deposit/	{ deposits += field("amount");next; }
     /(^|\n)check/	{ check += field("amount");next; }
     END		{ printf("deposits %.2f,checks $%.2f\n",deposits,check)}
     function field(name,i,f){
	     for(i=1;i<=NF;i++){
		     split($i,f," ")
		     if(f[1] == name)
			     return f[2]
	     }
	     #printf("error: no field %s in record\n%s\n",name,$0)
     }' $@


