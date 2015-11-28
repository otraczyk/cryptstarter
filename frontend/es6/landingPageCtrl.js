
cryptStarterApp.controller('landingController', ['$scope', '$auth',
  function ($scope, $auth) {

    this.authenticate = function (provider) {
      $auth.authenticate(provider);
    };

}]);
