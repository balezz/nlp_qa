$(function(){
	$('button').click(function(){
		$.ajax({
			url: '/wave',
			data: 'war.wav',
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
}); 
