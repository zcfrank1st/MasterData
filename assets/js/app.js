/**
 * Created by zcfrank1st on 7/14/15.
 */
var app = angular.module('myapp', ['ngResource','ngTable']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});