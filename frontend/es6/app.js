
let cryptStarterApp = angular.module('cryptStarter.app', [
  'ui.router'])
  .config(['$stateProvider',
           '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {
      $urlRouterProvider.otherwise('/');
      $stateProvider
        .state('landingPageState', {
          url: '/',
          templateUrl: 'partials/landingPageTpl.html',
          controller: 'landingController',
          controllerAs: 'LC'
        })
        .state('profileState', {
          url: '/profile',
          templateUrl: 'partials/profileTpl.html',
          controller: 'profileController',
          controllerAs: 'PC'
        })
        .state('contactsState', {
          url: '/contacts',
          templateUrl: 'partials/contactsTpl.html',
          controller: 'contactsController',
          controllerAs: 'CC'
        })
  }]);
