/**
 * Created by zcfrank1st on 7/14/15.
 */
app.controller('mdsController', function ($scope, $filter, ngTableParams) {
    var data = [{name: "test", id: 1},
            {name: "Tiancum", id: 43},
            {name: "Jacob", id: 27},
            {name: "Nephi", id: 29},
            {name: "Enos", id: 34},
            {name: "Tiancum", id: 43},
            {name: "Jacob", id: 27},
            {name: "Nephi", id: 29},
            {name: "Enos", id: 34},
            {name: "Tiancum", id: 43},
            {name: "Jacob", id: 27},
            {name: "Nephi", id: 29},
            {name: "Enos", id: 34},
            {name: "Tiancum", id: 43},
            {name: "Jacob", id: 27},
            {name: "Nephi", id: 29},
            {name: "Enos", id: 34}];  // json array

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