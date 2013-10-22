'use strict';

var app = angular.module('app', [
  'chieffancypants.loadingBar'
]);

app.controller('FormCtrl', [
  '$scope', '$element', '$http',
  function FormCtrl($scope, $element, $http) {

  $scope.submit = function() {
    var post_data = {
      url: $scope.url,
      extend: true
    };

    $http
    .post('/api/find_images/', post_data)
    .success(function(data, status, headers, config) {
      // this callback will be called asynchronously
      // when the response is available
      $scope.result = data;
      $scope.pre_class = '';
    })
    .error(function(data, status, headers, config) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
      $scope.result = data;
      $scope.pre_class = 'error_response';
    });
  };

  $scope.clear = function() {
    $scope.pre_class = '';
    $scope.result = 'Enter a link and press the blue button.';
    $scope.url = undefined;
  };

  $scope.clear();

  $scope.url = 'http://www.wendyslookbook.com/2013/10/color-love-rose-car-coat-purple-peplum/';

}]);

app.controller('ResultCtrl', ['$scope', '$element', '$http', function FormCtrl($scope, $element, $http) {

}]);
