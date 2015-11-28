'use strict';

var cryptStarterApp = angular.module('cryptStarter.app', ['ui.router', 'satellizer']).config(['$stateProvider', '$urlRouterProvider', '$authProvider', function ($stateProvider, $urlRouterProvider, $authProvider) {
  $urlRouterProvider.otherwise('/');
  $stateProvider.state('landingPageState', {
    url: '/',
    templateUrl: 'partials/landingPageTpl.html',
    controller: 'landingController',
    controllerAs: 'LC'
  }).state('profileState', {
    url: '/profile',
    templateUrl: 'partials/profileTpl.html',
    controller: 'profileController',
    controllerAs: 'PC'
  }).state('contactsState', {
    url: '/contacts',
    templateUrl: 'partials/contactsTpl.html',
    controller: 'contactsController',
    controllerAs: 'CC'
  });

  $authProvider.facebook({
    clientId: '1194316053918870',
    url: '/api/auth'
  });

  $authProvider.loginUrl = '/api/auth';
}]);