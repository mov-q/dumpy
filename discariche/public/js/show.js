function getDumpTitle(t) {
    $('#card-title').html(t);
};

function getDumpDescription(d) {
    $('#card-subtitle').html(d);
};

function getDumpHistory(d) {
    $('#card-history').html(d);
};

function getPosition(lat, lng) {
    $('#latitude').html(lat);
    $('#longitude').html(lng);
};

function getDumpDest(ddata) {
    hstr = '';
    $.each(ddata.res, function(i,item){
        if (item.sd == null)
            item.sd = 'Sconosciuto';
        if (item.ed == null)
            item.ed == 'ad ora';
        if (item.notes == null)
            item.notes = '';
        hstr += '<div class="info-entry"> \
                    <div class="info-item">Dal: </div> '+item.sd+' \
                    <div class="info-item"> al: </div> '+item.ed+' \
                    <div class="info-item">Destinazione: </div>'+item.type+' \
                </div> \
                <div class="info-notes"> \
                    '+item.notes+' \
                </div>';
    });
    $('#dest').html(hstr);
};

function getDumpAgent(adata) {
    hstr = '';
    $.each(adata.res, function(i,item){
        if (item.sd == null)
            item.sd = 'Sconosciuto';
        if (item.ed == null)
            item.ed == 'ad ora';
        if (item.notes == null)
            item.notes = '';
        hstr += '<div class="info-entry"> \
                    <div class="info-item">Dal: </div> '+item.sd+' \
                    <div class="info-item"> al: </div> '+item.ed+' \
                    <div class="info-item">Proprietà/Gestione: </div>'+item.name+' \
                </div> \
                <div class="info-notes"> \
                    '+item.notes+' \
                </div>';
    });
    $('#agent').html(hstr);
};

function getDumpStatus(sdata) {
    hstr = '';
    $.each(sdata.res, function(i,item){
        if (item.sd == '')
            item.sd = 'Sconosciuto';
        if (item.ed == '')
            item.ed == 'ad ora';
        if (item.notes == '')
            item.notes = '';
        hstr += '<div class="info-entry"> \
                    <div class="info-item">Dal: </div> '+item.sd+' \
                    <div class="info-item"> al: </div> '+item.ed+' \
                    <div class="info-item">Status: </div>'+item.desc+' \
                </div> \
                <div class="info-notes"> \
                    '+item.notes+' \
                </div>';
    });
    $('#status').html(hstr);
};

function getDumpQty(qdata) {
    hstr = '';
    $.each(qdata.res, function(i,item){
        if (item.sd == null)
            item.sd = 'Sconosciuto';
        if (item.ed == null)
            item.ed == 'ad ora';
        if (item.notes == null)
            item.notes = '';
        hstr += '<div class="info-entry"> \
                    <div class="info-item">Dal: </div> '+item.sd+' \
                    <div class="info-item"> al: </div> '+item.ed+' \
                    <div class="info-item">Quantità trattata: </div>'+item.type+' \
                </div> \
                <div class="info-notes"> \
                    '+item.notes+' \
                </div>';
    });
    $('#qty').html(hstr);
};


function loadNode(n) {
    $('#show-info').fadeOut(300, function(){
    });   
    $('#card-history').fadeOut(300, function(){
    });   
    
    $.post('/show/getNodeInfo', { node: n} , function(data) {
        getDumpTitle(data.title);
        getDumpDescription(data.desc);
        getDumpHistory(data.history);
        getPosition(data.latitude, data.longitude);
    }, "json");
    
    $.post('/show/getNodeDest', { node: n} , function(destdata) {
        getDumpDest(destdata);
    }, "json");
    
    $.post('/show/getNodeAgent', { node: n} , function(agdata) {
        getDumpAgent(agdata);
    }, "json");
    
    $.post('/show/getNodeStatus', { node: n} , function(stdata) {
        getDumpStatus(stdata);
    }, "json");
    
    $.post('/show/getNodeQuantity', { node: n} , function(qtydata) {
        getDumpQty(qtydata);
    }, "json");
    
    $('#show-info').fadeIn(500, function(){
    });   
    $('#card-history').fadeIn(500, function(){
    });   
};

function initialize() {
   
    var latlng = new google.maps.LatLng(40.912994, 14.289436);
    var myOptions = {
        zoom: 8,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.HYBRID
    };
    var dmap = new google.maps.Map(document.getElementById("show-map"),
                                    myOptions);
    
    $.getJSON('/show/getCoords', function(data){
        $.each(data.res, function(i,item){
            // qui prendo item.longitude e latitude
            var marklatlng = new google.maps.LatLng(item.latitude,item.longitude);
            var marker = new google.maps.Marker({
                        position: marklatlng, 
                        map: dmap, 
                        title: item.title,
                        clickable: true
                        });
            marker.value = item.id;
            google.maps.event.addListener(marker, "click", (function(marker) { return function() {
                loadNode(marker.value);
            }})(marker));

        });
    });


    //var kmlOptions = {map: "dmap"};
    //var kmlUrl = 'http://shift-left.net/discmap.kml';
    //var kml = new google.maps.KmlLayer(kmlUrl);
    //kml.setMap(dmap); 
};


