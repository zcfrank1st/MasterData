/**
 * Created by zcfrank1st on 7/14/15.
 */
app.controller('mdsController', function ($scope, $filter, ngTableParams, $resource) {
    var Tables = $resource('/mds/query/tables/');
    Tables.query({}, function (d) {
        var data = d;
        $scope.tableParams = new ngTableParams({
            page: 1,            // show first page
            count: 10          // count per page
        }, {
            total: data.length, // length of data
            getData: function($defer, params) {
                // use build-in angular filter
                var orderedData = params.filter() ?
                        $filter('filter')(data, params.filter()) :
                        data;

                $scope.datas = orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count());

                params.total(orderedData.length); // set total for recalc pagination
                $defer.resolve($scope.datas);
            }
        });
    });
});