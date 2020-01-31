let info = document.getElementsByClassName('form-control');
let data={}


function storeInfo(){
	for (item of info){
		data[item.getAttribute("name")] = item.value;
		data[item.getAttribute("name")] = item.value;
		data[item.getAttribute("name")] = item.value;
		data[item.getAttribute("name")] = item.value;
		data[item.getAttribute("name")] = item.value;
		data[item.getAttribute("name")] = item.value;
	}
	console.log(data);

}