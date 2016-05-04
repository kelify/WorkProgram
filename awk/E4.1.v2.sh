#!/bin/bash

awk '{printf("%s:%s:%d:%d:%.1f\n",$4,$1,$3,$2,1000*$3/$2)| "sort -t: +0 -1 +4rn"}' countries | awk 'BEGIN{FS=":";printf("%-15s %-10s %10s %7s %12s\n","CONTINENT","COUNTRY","POPULATION","AREA","POP.DEN.")}\
{ if($1 != prev ){
	print ""
	prev = $1
	if(prev != Total){
	if(NR != 1)
		printf("%-27s %7s %10s %10.1f\n\n","TOTAL FOR "Total,sum_poplucation,sum_area,sum_pop)
	Total = prev
	sum_poplucation = 0
	sum_area = 0
	sum_pop = 0
}
	sum_poplucation +=$3
	sum_area +=$4
	sum_pop +=$5

}
	else{
		$1 = ""
		sum_poplucation +=$3
		sum_area +=$4
		sum_pop +=$5
	}
printf("%-15s %-10s %7s %10s %10.1f\n",$1,$2,$3,$4,$5)
}
END{
printf("%-27s %7s %10s %10.1f\n\n","TOTAL FOR "Total,sum_poplucation,sum_area,sum_pop)	
}'

