let basePath = './';

(function () {
  'use strict';

  angular.module('appModule', [
    'ui.router',
    'ngMaterial',
    'ngAnimate',
    'ngCookies'
  ])
  .config(function ($httpProvider) {
    $httpProvider.defaults.headers.common = {};
    $httpProvider.defaults.headers.post = {};
    $httpProvider.defaults.headers.put = {};
    $httpProvider.defaults.headers.patch = {};
  })
  .run(function($rootScope){
    // $rootScope.serverUrl = 'http://192.168.43.136:8000/';
    $rootScope.serverUrl = '';
  })
  // .run(['$rootScope', '$location', '$cookieStore', '$http',
  //   function ($rootScope, $location, $cookies, $http) {
  //     $rootScope.serverUrl = 'http://192.168.137.135:8000/';
  //     // keep user logged in after page refresh
  //     $rootScope.globals = $cookies.get('globals') || {};
  //     if ($rootScope.globals.currentUser) {
  //       $http.defaults.headers.common['Authorization'] =
  //         'Basic ' + $rootScope.globals.currentUser.authdata;
  //     }
  //   }
  // ])
  
})();