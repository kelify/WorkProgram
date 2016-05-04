


awk '
function max(m,n){
	panshen=10
	return m > n ? m:n
}
BEGIN{

print max(10,20),panshen
}'








