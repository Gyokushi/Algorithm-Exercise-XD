// calculate the addition of two binary number

function Bi_Add(a,b,l){
	c = new Array(l+1);
	var flag = 0;
	i = l-1;
	do{
		c[i+1] = a[i]^b[i]^flag;
		flag = (c[i+1]?a[i]&&b[i]&&flag:a[i]||b[i]||flag);
	}while(i-->0);
	c[0] = flag;
	console.log(c.join(" "))
}

var a = new Array(10);
var b = new Array(10);
for(var i =0;i<a.length;i++){
	a[i] = Math.floor(Math.random()*2);
	b[i] = Math.floor(Math.random()*2)
}
console.log("  "+a.join(" "));
console.log("  " + b.join(" "));
Bi_Add(a,b,a.length);
