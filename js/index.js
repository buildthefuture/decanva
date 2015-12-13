// JavaScript Document
'strict use'
$(document).ready(function(){
	
	var loaded = false;
	
	var waitImagePath = "images/wait.png"
	
	var preloadImage2 = new Image();
	preloadImage2.src = "images/wait.png";
	
	var preloadImage = new Image();
	preloadImage.src = "images/wait.gif";
	imagesLoaded( preloadImage, function() {
		console.log("waiting gif has been loaded");
		waitImagePath = "images/wait.gif"
	});
	
	$(".submitButton").click(function() {
		var searchInput = $("#searchForm input").val();
		var dataString = "&search="+searchInput;
		search(dataString, searchInput);
	});
	
	$(".feedbackButton").click(function() {
		var searchInput = $("#resultImage").attr("data-content");
		var dataString = "&search="+searchInput+"&addition=bad";
		search(dataString, searchInput);
	});
	
	$('#resultImage').bind('error', function(e){
		$(".feedbackButton").hide();
		$("#noresultMessage").hide();
		$("#resultImage").attr("src",  waitImagePath);
		$("#waitMessage").show();
		var searchInput = $("#resultImage").attr("data-content");
		var dataString = "&search="+searchInput+"&addition=bad";
		search(dataString, searchInput);
	});
	
	$("#searchText").keydown(function(event){
		console.log(event.keyCode);
    	if(event.keyCode == 13){
			event.preventDefault();
        	$(".submitButton").click();
    	}
	});
	
	function search(dataString, searchInput) {
		loaded = false;
		if (searchInput != "") {
			setTimeout(function () {
				if (!loaded) {
					$(".feedbackButton").hide();
					$("#noresultMessage").hide();
					$("#resultImage").attr("src",  waitImagePath);
					$("#waitMessage").show();
				}
			}, 1000);
		  	console.log(dataString);
		  	$.ajax({
				type:"GET",
			  	url:"search.php",
			  	data: dataString,
			  	cache: false,
				error: function(xhr, status, error) {
					console.log("An error occured: " + xhr + " " + status + " " + error);
				},
				success: function(result, status, xhr) {
					console.log(result + status + xhr);
					var imgsrc = result.split(">>>>").pop();
					if (imgsrc != "\n") {
					  $("#resultImage").attr("src", imgsrc).attr("data-content", searchInput);
					  loaded = true;
					  $("#imageDiv").imagesLoaded(function() {
						  $("#waitMessage").hide();
						  $(".feedbackButton").show();
						  $("#noresultMessage").hide();
					  });
					}
					else {
						$("#resultImage").attr("src", "images/empty.jpg");
						$("#waitMessage").hide();
						$("#noresultMessage").show();
					}
			  } 
		  });
		}
	}
});