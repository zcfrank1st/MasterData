/**
 * Created by zcfrank1st on 7/14/15.
 */
app1.controller('mdsController1', function ($scope, $location, $resource) {
    var saveDescription = $resource('/mds/change/desc');
    var saveColumnInfo = $resource('/mds/change/desc/column');

    var currentUrl = $location.absUrl();
    var id = currentUrl.substr(currentUrl.length - 2, 1);

    $scope.description = true;
    $scope.saveContent = function () {
        var data = {id: id, description: $scope.descriptionInfo};
        saveDescription.save(data, function (r) {
            if (r.info === "yes") {
                location.href=$location.absUrl();
            } else if(r.info === "no") {
                $scope.descAlert = true;

            } else {
                $scope.descAlert = true;
            }
        });
    };

    
});