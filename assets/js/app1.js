/**
 * Created by zcfrank1st on 7/14/15.
 */
var app1 = angular.module('myapp1', ['ngResource']);

app1.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});