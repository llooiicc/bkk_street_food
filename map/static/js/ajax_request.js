function sendBounds(data){
	
	$.post('/map/bounds/', data, function(data) {
		console.log(data)
	})
}