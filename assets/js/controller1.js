/**
 * Created by zcfrank1st on 7/14/15.
 */
app1.controller('mdsController1', function ($scope, $location, $resource) {
    var saveDescription = $resource('/mds/change/desc');
    var saveColumnInfo = $resource('/mds/change/desc/column');
    var getColumnNumber = $resource('/mds/get/columnnumber/:id/', {id: '@id'});

    var currentUrl = $location.absUrl();
    var id = currentUrl.substr(currentUrl.length - 2, 1);

    $scope.description = true;
    $scope.saveContent = function () {
        var data = {id: id, description: $scope.descriptionInfo};
        saveDescription.save(data, function (r) {
            if (r.info === "yes") {
                location.href = $location.absUrl();
            } else if (r.info === "no") {
                $scope.descAlert = true;
            } else {
                $scope.descAlert = true;
            }
        });
    };



    $scope.columnDescription = true;
    $scope.saveColumnInfo = function () {
        getColumnNumber.get({id: id}, function (res) {
            var valueList = [];
            for (var i = 1; i <= res.number; i ++) {
                $(document).ready(function () {
                    valueList.push($('#row' + i).val());
                });
            }
            var data = {id: id, column: valueList};
            saveColumnInfo.save(data, function (r) {
                if (r.info === "yes") {
                    location.href = $location.absUrl();
                } else if (r.info === "no") {
                    $scope.columnDescAlert = true;
                } else {
                    $scope.columnDescAlert = true;
                }
            });
        });
    };


});