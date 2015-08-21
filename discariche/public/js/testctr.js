function initialize() {
   
    var latlng = new google.maps.LatLng(40.60, 14.16);
    var myOptions = {
        zoom: 9,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    var dmap = new google.maps.Map(document.getElementById("map-show"),
                                    myOptions);
    
    $.getJSON('/testctr/getCoords', function(data){
        $.each(data.res, function(i,item){
            // qui prendo item.longitude e latitude
            var marklatlng = new google.maps.LatLng(item.latitude,item.longitude);
            var marker = new google.maps.Marker({
                        position: marklatlng, 
                        map: dmap, 
                        title: item.title
                        });   
        });
    });


    //var kmlOptions = {map: "dmap"};
    //var kmlUrl = 'http://shift-left.net/discmap.kml';
    //var kml = new google.maps.KmlLayer(kmlUrl);
    //kml.setMap(dmap); 
}
