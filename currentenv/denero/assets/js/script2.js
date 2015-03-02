
function processSearch(){
	 var search = document.search.texter.value;
	 document.getElementById("searchR").innerHTML += search;
	 window.location.href = 'result.html'; 
	}
