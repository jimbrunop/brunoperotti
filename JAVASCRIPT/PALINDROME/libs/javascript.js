$(document).ready(function() {
	 var testPoli = function (string) {
	    if (string == string.split('').reverse().join('')) {
	        alert(string + " is palindrome");
	    }
	    else {
	        alert(string + " is not palindrome");
	    }
	}

  $(".submit").click(function () {
	   	testPoli(document.getElementById('inputTxt').value);
	    return false;
	});
});