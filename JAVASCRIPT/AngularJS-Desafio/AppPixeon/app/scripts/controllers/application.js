'use strict';

/**
 * @ngdoc function
 * @name appPixeonApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the appPixeonApp
 */
angular.module('appPixeonApp')
  .controller('AboutCtrl', function () {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];


    var arrayTxt = {};
    var arrayNumber = {};


   	var storedValue = localStorage.getItem("username");

   	 $("p.txtUserPrint").append(storedValue);



    $('.doIt').attr('disabled',true);
    $('.doItCombin').attr('disabled',true);
      $('.activeInputNumb').keyup(function(){
        if($(this).val().length !=0){
            $('.doIt').attr('disabled', false);            
        }else{
            $('.doIt').attr('disabled',true);
        }
    });


    $(".doIt").click(function() {

    	$('.doItCombin').attr('disabled',false);

	  $(".activeInput").each(function() {
	 		arrayTxt[$(this).attr("name")] = $(this).val().split(' ');

	 			   $("ul.txt").append(arrayTxt[$(this).attr("name")] + " ");

		});

	  $(".activeInputNumb").each(function(){
	  		arrayNumber[$(this).attr("name")] = $(this).val();
	  			$(function(){
	  				parseInt($(this).val());
	  			});
	  		
	  	});
	});

    $(".doItCombin").click(function() {
			
	  	
	});

	

  });
