const arr = [5,0,9,1,7,4,2,6,3,8];
var holder = 0;

for (var i=0; i<arr.length; i++) {
	for (var j=i; j<arr.length; j++) {
		if (arr[i]<arr[j]) {
			holder = arr[i];
			arr[i] = arr[j];
			arr[j] = holder;
		}
	}	
}
console.log(arr);
console.log(arr.toString());


// OR reverse order:

for (var i=0; i<arr.length; i++) {
	for (var j=i; j<arr.length; j++) {
		if (arr[i]>arr[j]) {
			holder = arr[i];
			arr[i] = arr[j];
			arr[j] = holder;
		}
	}	
}
console.log(arr);
console.log(arr.toString());