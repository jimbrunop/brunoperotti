'use strict';

/**
 * @ngdoc function
 * @name appPixeonApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the appPixeonApp
 */
angular.module('appPixeonApp')
  .controller('LoginCtrl', function () {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

   var input = $("#username");
	

		 $(".btn-login").click(function() {
		 	localStorage.setItem("username", input.val());
		});

  });
