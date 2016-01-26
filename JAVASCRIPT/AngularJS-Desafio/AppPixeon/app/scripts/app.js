'use strict';

/**
 * @ngdoc overview
 * @name appPixeonApp
 * @description
 * # appPixeonApp
 *
 * Main module of the application.
 */
angular
  .module('appPixeonApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl',
        controllerAs: 'login'
      })
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl',
        controllerAs: 'login'
      })
      .when('/application', {
        templateUrl: 'views/application.html',
        controller: 'AboutCtrl',
        controllerAs: 'application'
      })
      .otherwise({
        redirectTo: '/'
      });

    

        

  });

