function dpset() {
    $(".datepick").datepicker({ 
        dateFormat: 'dd/mm/yy', 
        changeMonth: true,
        changeYear: true,
        yearRange: '1950:c+10'
     });
};

function doDumpTypeCompl() {
    $(".dumptype-auto").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/dumptype/dumptype_jac",
                contentType: "application/json",
                dataType: "json",
                data: {
                    input: request.term
                },
                success: function( data ) {
                    response($.map(data.res, function(item) {
                        return {
                            label: item.type,
                            value: item.type,
                            idvalue: item.id
                        }
                    }));
                }
            });
        },
        minLength: 2,

        select: function(event, ui) {
            setid = '#dumptype-auto-id-'+tform;
            $(setid).attr("value",ui.item.idvalue);
        },
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
};

$(function() {
    $(".datepick").datepicker({ 
        dateFormat: 'dd/mm/yy', 
        changeMonth: true,
        changeYear: true,
        yearRange: '1950:c+10'
     });
});


function addDumpTypeField() {
    if(typeof this.dtcounter == 'undefined'){
        //this.counter = document.getElementById("startauth").value;
        this.dtcounter = 0
    }
    // hide the button
    butid = '#dt-addbutton-'+this.dtcounter;
    $(butid).hide();
    this.dtcounter++;

    $("#new-dtfield").append(" \
        <div class='dt'> \
            <div class='form-row'> \
                <label for='type'>Start date:</label> \
                <input type='text' id='dt-start-date-"+this.dtcounter+"' name='dt-start-date-"+this.dtcounter+"' class='datepick'> \
            </div> \
            <div class='form-row'> \
                <label for='type'>End date:</label> \
                <input type='text' id='dt-end-date-"+this.dtcounter+"' name='dt-end-date-"+this.dtcounter+"' class='datepick'> \
            </div> \
            <div class='form-row'> \
                <label for='type'>Type:</label> \
                <input type='text' id='dumptype-auto-"+this.dtcounter+"' name='dumptype-auto-"+this.dtcounter+"' class='dumptype-auto' onfocus='tform="+this.dtcounter+"; doDumpTypeCompl();'> \
                <input type='hidden' name='dumptype-auto-id-"+this.dtcounter+"' id='dumptype-auto-id-"+this.dtcounter+"' value='-1'> \
            </div> \
            <div class='form-row'>\
                <label for='dt-note'>Notes:</label>\
                <textarea id='dt-notes-"+this.dtcounter+"' name='dt-notes-"+this.dtcounter+"'></textarea>\
                <div class='notes-counter'></div>\
            </div>\
            <a href='#' id='dt-addbutton-"+this.dtcounter+"' onclick='addDumpTypeField(); return false;'><img class='plus' src='/img/plus.png'></a><br /> \
        </div>");

                    
    $("#new-dtfield").show();
    dpset();

    return this.dtcounter;
};

function doAgentCompl() {
    $(".ag-auto").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/agent/agent_jac",
                contentType: "application/json",
                dataType: "json",
                data: {
                    input: request.term
                },
                success: function( data ) {
                    response($.map(data.res, function(item) {
                        return {
                            label: item.name,
                            value: item.name,
                            idvalue: item.id
                        }
                    }));
                }
            });
        },
        minLength: 2,

        select: function(event, ui) {
            setid = '#ag-auto-id-'+tform;
            $(setid).attr("value",ui.item.idvalue);
        },
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
};

function addAgentField() {
    if(typeof this.agcounter == 'undefined'){
        //this.counter = document.getElementById("startauth").value;
        this.agcounter = 0
    }
    // hide the button
    butid = '#ag-addbutton-'+this.agcounter;
    $(butid).hide();
    this.agcounter++;

    $("#new-agfield").append(" \
        <div class='agent'>\
            <div class='form-row'> \
                <label for='type'>Start date:</label>\
                <input type='text' id='ag-start-date-"+this.agcounter+"' name='ag-start-date-"+this.agcounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='type'>End date:</label>\
                <input type='text' id='ag-end-date-"+this.agcounter+"' name='ag-end-date-"+this.agcounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='type'>Agent:</label>\
                <input type='text' id='ag-auto-"+this.agcounter+"' name='ag-auto-"+this.agcounter+"' class='ag-auto' onfocus='tform="+this.agcounter+"; doAgentCompl();'>\
                <input type='hidden' name='ag-auto-id-"+this.agcounter+"' id='ag-auto-id-"+this.agcounter+"' value='-1'>\
            </div>\
            <div class='form-row'>\
                <label for='ag-note'>Notes:</label>\
                <textarea id='ag-notes-"+this.agcounter+"' name='ag-notes-"+this.agcounter+"'></textarea>\
                <div class='notes-counter'></div>\
            </div>\
            <a href='#' id='ag-addbutton-"+this.agcounter+"' onclick='addAgentField(); return false;'><img class='plus' src='/img/plus.png'></a><br />\
        </div>");

                    
    $("#new-agfield").show();
    dpset()

    return this.agcounter;
};

function addQtyField() {
    if(typeof this.qtycounter == 'undefined'){
        //this.counter = document.getElementById("startauth").value;
        this.qtycounter = 0
    }
    // hide the button
    butid = '#qty-addbutton-'+this.qtycounter;
    $(butid).hide();
    this.qtycounter++;

    $("#new-qtyfield").append(" \
        <div class='quantity'> \
            <div class='form-row'> \
                <label for='type'>Start date:</label> \
                <input type='text' id='qty-start-date-"+this.qtycounter+"' name='qty-start-date-"+this.qtycounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='type'>End date:</label>\
                <input type='text' id='qty-end-date-"+this.qtycounter+"' name='qty-end-date-"+this.qtycounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='type'>Quantity:</label>\
                <input type='text' id='qty-"+this.qtycounter+"' name='qty-"+this.qtycounter+"'>\
            </div>\
            <div class='form-row'>\
                <label for='qty-note'>Notes:</label>\
                <textarea id='qty-notes-"+this.qtycounter+"' name='qty-notes-"+this.qtycounter+"'></textarea>\
                <div class='notes-counter'></div>\
            </div>\
            <a href='#' id='qty-addbutton-"+this.qtycounter+"' onclick='addQtyField(); return false;'><img class='plus' src='/img/plus.png'></a><br />\
        </div>");

                    
    $("#new-qtyfield").show();
    dpset()

    return this.qtycounter;
};

function doStatusCompl() {
    $(".status-auto").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/status/status_jac",
                contentType: "application/json",
                dataType: "json",
                data: {
                    input: request.term
                },
                success: function( data ) {
                    response($.map(data.res, function(item) {
                        return {
                            label: item.desc,
                            value: item.desc,
                            idvalue: item.id
                        }
                    }));
                }
            });
        },
        minLength: 2,

        select: function(event, ui) {
            setid = '#st-auto-id-'+tform;
            $(setid).attr("value",ui.item.idvalue);
        },
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
};

function addStatusField() {
    if(typeof this.stcounter == 'undefined'){
        //this.counter = document.getElementById("startauth").value;
        this.stcounter = 0
    }
    // hide the button
    butid = '#st-addbutton-'+this.stcounter;
    $(butid).hide();
    this.stcounter++;

    $("#new-stfield").append(" \
        <div class='status'>\
            <div class='form-row'>\
                <label for='st_start_date'>Start date:</label>\
                <input type='text' id='st-start-date-"+this.stcounter+"' name='st-start-date-"+this.stcounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='st_end_date'>End date:</label>\
                <input type='text' id='st-end-date-"+this.stcounter+"' name='st-end-date-"+this.stcounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='status'>Status:</label>\
                <input type='text' id='st-auto-"+this.stcounter+"' name='st-auto-"+this.stcounter+"' class='status-auto' onfocus='tform="+this.stcounter+"; doStatusCompl();'>\
                <input type='hidden' name='st-auto-id-"+this.stcounter+"' id='st-auto-id-"+this.stcounter+"' value='-1'>\
            </div>\
            <div class='form-row'>\
                <label for='st-note'>Notes:</label>\
                <textarea id='st-notes-"+this.stcounter+"' name='st-notes-"+this.stcounter+"'></textarea>\
                <div class='notes-counter'></div>\
            </div>\
            <a href='#' id='st-addbutton-"+this.stcounter+"' onclick='addStatusField(); return false;'><img class='plus' src='/img/plus.png'></a><br />\
        </div>");

                    
    $("#new-stfield").show();
    dpset();

    return this.stcounter;
};

$(function(){
    $('#ddesc').keyup(function() {
        var max=128;
        if($(this).val().length > max) {
            $(this).val($(this).val().substr(0, max));
        }
        $('#ddesc-counter').html((max - $(this).val().length) + ' characters remaining');
    });
});

$(function(){
    $("#comune").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/comuni/comuni_jac",
                contentType: "application/json",
                dataType: "json",
                data: {
                    input: request.term
                },
                success: function( data ) {
                    response($.map(data.res, function(item) {
                        return {
                            label: item.name,
                            value: item.name,
                            idvalue: item.id
                        }
                    }));
                }
            });
        },
        minLength: 2,

        select: function(event, ui) {
            setid = '#comune-id';
            $(setid).attr("value",ui.item.idvalue);
        },
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
});

function doCerCompl() {
    $(".cer-auto").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/cercode/cer_jac",
                contentType: "application/json",
                dataType: "json",
                data: {
                    input: request.term
                },
                success: function( data ) {
                    response($.map(data.res, function(item) {
                        return {
                            label: item.desc,
                            value: item.desc,
                            idvalue: item.id
                        }
                    }));
                }
            });
        },
        minLength: 2,

        select: function(event, ui) {
            setid = '#cer-auto-id-'+tform;
            $(setid).attr("value",ui.item.idvalue);
        },
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
};

function addCerField() {
    if(typeof this.cercounter == 'undefined'){
        //this.counter = document.getElementById("startauth").value;
        this.cercounter = 0
    }
    // hide the button
    butid = '#cer-addbutton-'+this.cercounter;
    $(butid).hide();
    this.cercounter++;

    $("#new-cerfield").append(" \
        <div class='cer'>\
            <div class='form-row'>\
                <label for='cer'>CER code:</label>\
                <input type='text' id='cer-auto-"+this.cercounter+"' name='cer-auto-"+this.cercounter+"' class='cer-auto' size='45' onfocus='tform="+this.cercounter+"; doCerCompl();'>\
                <input type='hidden' name='cer-auto-id-"+this.cercounter+"' id='cer-auto-id-"+this.cercounter+"' value='-1'>\
            </div>\
            <a href='#' id='cer-addbutton-"+this.cercounter+"' onclick='addCerField(); return false;'><img class='plus' src='/img/plus.png'></a><br />\
        </div>");

                    
    $("#new-cerfield").show();
    dpset();

    return this.cercounter;
};

function addBibField() {
    if(typeof this.bibcounter == 'undefined'){
        //this.counter = document.getElementById("startauth").value;
        this.bibcounter = 0
    }
    // hide the button
    butid = '#bib-addbutton-'+this.bibcounter;
    $(butid).hide();
    this.bibcounter++;

    $("#new-bibfield").append(" \
        <div class='bib'>\
            <div class='form-row'>\
                <label for='bib'>Bib title:</label>\
                <input type='text' id='bib-title-"+bibcounter+"' name='bib-title-"+bibcounter+"' size='45'>\
            </div>\
            <div class='form-row'>\
                <label for='bib'>Bib url:</label>\
                <input type='text' id='bib-url-"+bibcounter+"' name='bib-url-"+bibcounter+"' size='60'>\
            </div>\
            <div class='form-row'>\
                <label for='bib'>Bib ref.date:</label>\
                <input type='text' id='bib-refdate-"+bibcounter+"' name='bib-refdate-"+bibcounter+"' class='datepick'>\
            </div>\
            <div class='form-row'>\
                <label for='bibtype'>Bib type:</label>\
                <select id='bib-type-"+bibcounter+"' name='bib-type-"+bibcounter+"'>\
                    <option value='text'>Text</option>\
                    <option value='audio'>Audio</option>\
                    <option value='video'>Video</option>\
                    <option value='photo'>Photo</option>\
                </select>\
            </div>\
            <a href='#' id='bib-addbutton-"+bibcounter+"' onclick='addBibField(); return false;'><img class='plus' src='/img/plus.png'></a><br />\
        </div>");

                    
    $("#new-bibfield").show();
    dpset();

    return this.bibcounter;
};

