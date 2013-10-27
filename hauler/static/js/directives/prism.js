angular.module('vinta.prism', [])

.directive('prism', [
  function() {
    return {
      restrict: 'E',
      template: '<pre><code ng-transclude ng-bind="result" class="language-javascript"></code></pre>',
      replace: true,
      transclude: true,
      link: function(scope, element, attrs) {
        scope.$watch('result', function() {
          Prism.highlightElement(element.find('code')[0]);
        });
      }
    };
  }
]);
