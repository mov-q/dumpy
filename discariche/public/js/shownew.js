var globmap;
var latlng = new google.maps.LatLng(40.912994, 14.289436);

function getDumpTitle(t) {
    $('#card-title').html(t);
};

function getDumpDescription(d) {
    $('#card-subtitle').html(d);
};

function getDumpHistory(d) {
    $('#card-history').html(d);
};

function getPosition(lat, lng, com, prov) {
    latstr =    '<div class="info-entry"> \
                    <div class="info-item">Latitudine: </div>'+lat+'\
                 </div> \
                 <div class="info-entry"> \
                    <div class="info-item">Longitudine: </div>'+lng+'\
                 </div> \
                 <div class="info-entry"> \
                    <div class="info-item">Comune: </div>'+com+'\
                 </div> \
                 <div class="info-entry"> \
                    <div class="info-item">Provincia: </div>'+prov+'\
                 </div>';
    $('#geninfo').html(latstr);
};

function getDumpCer(cdata) {
    hstr = '';
    $.each(cdata.res, function(i,item){
        hstr += '<div class="info-entry"> \
                    <div class="info-item">Codice: </div> '+item.code+' \
                    <div class="info-item">Descrizione: </div>'+item.desc+' \
                </div>';
    });
    if (hstr != '')
        hstr = '<div class="info-title">Codici CER</div>'+hstr;
    $('#cer').html(hstr);
};

function getDumpBiblio(bibdata) {
    hstr = '';
    $.each(bibdata.res, function(i,item){
        hstr += '<div class="info-entry"> \
                    <div class="info-item">'+item.date+' - '+item.type+': </div>\
                    <a href="'+item.url+'" target="_new">'+item.desc+'</a>\
                </div>';
    });
    if (hstr != '')
        hstr = '<div class="info-title">Bibliografia Media</div>'+hstr;
    $('#biblio').html(hstr);
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
    if (hstr != '')
        hstr = '<div class="info-title">Destinazioni</div>'+hstr;
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
    if (hstr != '')
        hstr = '<div class="info-title">Gestione</div>'+hstr;
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
    if (hstr != '')
        hstr = '<div class="info-title">Status</div>'+hstr;
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
                    <div class="info-item">Quantità trattata: </div>'+item.qty+' \
                </div> \
                <div class="info-notes"> \
                    '+item.notes+' \
                </div>';
    });
    if (hstr != '')
        hstr = '<div class="info-title">Quantità</div>'+hstr;
    $('#qty').html(hstr);
};

function loadNode(n) {
    $('#show-info').fadeOut(300, function(){
    });   
    $('#card-history').fadeOut(300, function(){
    });   
    $('#show-about').fadeOut(300, function(){
    });   
    $('#show-home').fadeOut(300, function(){
    });   
    
    $.post('/show/getNodeInfo', { node: n} , function(data) {
        getDumpTitle(data.title);
        getDumpDescription(data.desc);
        getDumpHistory(data.history);
        getPosition(data.latitude, data.longitude, data.com, data.prov);
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
    $.post('/show/getNodeCer', { node: n} , function(cerdata) {
        getDumpCer(cerdata);
    }, "json");
    $.post('/show/getNodeBiblio', { node: n} , function(bibdata) {
        getDumpBiblio(bibdata);
    }, "json");
    
    
    $('#show-info').fadeIn(500, function(){
    });   
    $('#card-history').fadeIn(500, function(){
    });   
    
};

function loadNodeAndZoom(n) {
    $('#show-info').fadeOut(300, function(){
    });   
    $('#card-history').fadeOut(300, function(){
    });   
    $('#show-about').fadeOut(300, function(){
    });   
    $('#show-home').fadeOut(300, function(){
    });   
    
    $.post('/show/getNodeInfo', { node: n} , function(data) {
        getDumpTitle(data.title);
        getDumpDescription(data.desc);
        getDumpHistory(data.history);
        getPosition(data.latitude, data.longitude, data.com, data.prov);
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
    $.post('/show/getNodeCer', { node: n} , function(cerdata) {
        getDumpCer(cerdata);
    }, "json");
    $.post('/show/getNodeBiblio', { node: n} , function(bibdata) {
        getDumpBiblio(bibdata);
    }, "json");
    
    $('#show-info').delay(800).fadeIn(500, function(){
    });
    $('#card-history').fadeIn(500, function(){
    });   
};


function initialize() {
   
    var myOptions = {
        zoom: 9,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.HYBRID
    };
    var dmap = new google.maps.Map(document.getElementById("map-container"),
                                    myOptions);
    globmap = dmap;
    
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
                var cur_to = marker.getPosition();
                nlng = cur_to.lng()-0.0045;
                nlat = cur_to.lat();
                zmto = new google.maps.LatLng(nlat,nlng);
                dmap.panTo(zmto);
                dmap.setZoom(17);
                loadNodeAndZoom(marker.value);
            }})(marker));
            google.maps.event.addListener(marker, "rightclick", (function(marker) { return function() {
                loadNode(marker.value);
            }})(marker));
        });
    });


    //var kmlOptions = {map: "dmap"};
    //var kmlUrl = 'http://shift-left.net/discmap.kml';
    //var kml = new google.maps.KmlLayer(kmlUrl);
    //kml.setMap(dmap); 
};

$(document).keydown(function(e) {
    if (e.keyCode == 27) { 
        $('#show-info').fadeOut(300, function() {
        });
        $('#show-about').fadeOut(300, function() {
        });
        $('#show-home').fadeOut(300, function() {
        });
    } 
});

function hideAllOlay() {
    $('#show-info').fadeOut(100);
    $('#show-home').fadeOut(100);
    $('#show-contact').fadeOut(100);
};

function showHomeOlay() {
    hideAllOlay();
    $('#show-home').fadeIn(500);
};

function showContactOlay() {
    hideAllOlay();
    $('#show-contact').fadeIn(500);
};

function resetMap() {
    hideAllOlay();
    globmap.panTo(latlng);
    globmap.setZoom(9);
};

$(document).ready( function() {
    $('.menu-item').hover(  function () {
            $(this).css({color: '#15ff00'});
            alert(green);
        }, 
        function () {
            $(this).css({color: '#ffffff' });
    });
});
