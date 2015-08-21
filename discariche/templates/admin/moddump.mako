<%inherit file="/admin/admin.mako" />
<div class="generic-form">
    <div class="title">Add a dump</div>
    ${h.form(url(controller='admin', action='modsubmit'), method='POST', id='frm-adddump')}
        <input type='hidden' name='mainid' id='mainid' value='${c.dump.id}'> 
        <div class="form-row">
            <label for='name'>Name:</label>
            <input type="text" id="name" name="name" value="${c.dump.name}" size="35">
        </div>
        <div class="form-row">
            <label for='latitude'>Latitude:</label>
            <input type="text" id="latitude" name="latitude" value="${c.dump.latitude}">
        </div>
        <div class="form-row">
            <label for='longitude'>Longitude:</label>
            <input type="text" id="longitude" name="longitude" value="${c.dump.longitude}" >
        </div>
        <div class="form-row">
            <label for="comune">Comune:</label>
            % if c.comune:
                <input type="text" id="comune" name="comune" value="${c.comune.denominazione}">
                ${h.hidden('comune-id', c.dump.comune,'comune-id')}
            % else:
                <input type="text" id="comune" name="comune">
                ${h.hidden('comune-id','','comune-id')}
            % endif
        </div>
        <div class="form-row">
            <label for='ddesc'>Brief description:</label>
            <textarea id="ddesc" name="ddesc" rows="5" cols="35">${c.dump.description}</textarea>
            <div id="ddesc-counter"></div>
        </div>
        <div class="form-row">
            <label for='history'>History (can use html):</label>
            <textarea id="history" name="history" class="history">${c.dump.history}</textarea>
        </div>
        <br /><br />
        
        <div class="section-title">Existing dump-status entries</div>
        % for i in c.statusdump:
            <div id="sd-modview-${i.sd_id}">
                From: ${i.st_sdate} To: ${i.st_edate}: Status: ${i.st_desc}  Notes: ${i.st_notes} 
                <img onclick="deleteStatusDump(${i.sd_id});" class="minus" alt="remove item" src='/img/minus.png' />
            </div>
        % endfor
        <div class="section-title">Add here dump status over-time</div>
        <div class="status"> 
            <div class="form-row">
                <label for='st_start_date'>Start date:</label>
                <input type="text" id="st-start-date-0" name="st-start-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='st_end_date'>End date:</label>
                <input type="text" id="st-end-date-0" name="st-end-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='status'>Status:</label>
                <input type="text" id="st-auto-0" name="st-auto-0" class="status-auto" onfocus="tform=0; doStatusCompl();">
                <input type="hidden" name="st-auto-id-0" id="st-auto-id-0" value="-1">
            </div>
            <div class="form-row">
                <label for='st-note'>Notes:</label>
                <textarea id='st-notes-0' name='st-notes-0'></textarea>
                <div class="notes-counter"></div>
            </div>
            <a href="#" id='st-addbutton-0' onclick='addStatusField(); return false;'><img class="plus" src="/img/plus.png"></a><br />
        </div>
        <div id="new-stfield">
        </div>
        <div class="section-title">Existing dump destination entries</div>
        % for i in c.dumptype:
            <div id="dt-modview-${i.re_id}">
                From: ${i.dt_sdate} To: ${i.dt_edate}: Type: ${i.dt_type}  Notes: ${i.dt_notes} 
                <img onclick="deleteReallocation(${i.re_id});" class="minus" alt="remove item" src='/img/minus.png' />
            </div>
        % endfor
        <div class="section-title">Add here dump destination over time</div>
        <div class="dt"> 
            <div class="form-row">
                <label for='dt_start_date'>Start date:</label>
                <input type="text" id="dt-start-date-0" name="dt-start-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='dt_end_date'>End date:</label>
                <input type="text" id="dt-end-date-0" name="dt-end-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='type'>Type:</label>
                <input type="text" id="dumptype-auto-0" name="dumptype-auto-0" class="dumptype-auto" onfocus="tform=0; doDumpTypeCompl();">
                <input type="hidden" name="dumptype-auto-id-0" id="dumptype-auto-id-0" value="-1">
            </div>
            <div class='form-row'>
                <label for='dt-note'>Notes:</label>
                <textarea id='dt-notes-0' name='dt-notes-0'></textarea>
                <div class='notes-counter'></div>
            </div>
            <a href="#" id='dt-addbutton-0' onclick='addDumpTypeField(); return false;'><img class="plus" src="/img/plus.png"></a><br />
        </div>
        <div id="new-dtfield">
        </div>
        <div class="section-title">Existing dump agent entries</div>
        % for i in c.agentdump:
            <div id="ag-modview-${i.ad_id}">
                From: ${i.ag_sdate} To: ${i.ag_edate}: Name: ${i.ag_name}  Notes: ${i.ag_notes} 
                <img onclick="deleteAgentDump(${i.ad_id});" class="minus" alt="remove item" src='/img/minus.png' />
            </div>
        % endfor
        <div class="section-title">Add here dump agents overtime</div>
        <div class="agent"> 
            <div class="form-row">
                <label for='ag_start_date'>Start date:</label>
                <input type="text" id="ag-start-date-0" name="ag-start-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='ag_end_date'>End date:</label>
                <input type="text" id="ag-end-date-0" name="ag-end-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='agent'>Agent:</label>
                <input type="text" id="ag-auto-0" name="ag-auto-0" class="ag-auto" onfocus="tform=0; doAgentCompl();">
                <input type="hidden" name="ag-auto-id-0" id="ag-auto-id-0" value="-1">
            </div>
            <div class='form-row'>
                <label for='ag-note'>Notes:</label>
                <textarea id='ag-notes-0' name='ag-notes-0'></textarea>
                <div class='notes-counter'></div>
            </div>
            <a href="#" id='ag-addbutton-0' onclick='addAgentField(); return false;'><img class="plus" src="/img/plus.png"></a><br />
        </div>
        <div id="new-agfield">
        </div>
        <div class="section-title">Existing dump quantity entries</div>
        % for i in c.qtydump:
            <div id="qty-modview-${i.qty_id}">
                From: ${i.qty_sdate} To: ${i.qty_edate} Quantity: ${i.qty_quantity} Notes: ${i.qty_notes}
                <img onclick="deleteQuantity(${i.qty_id});" class="minus" alt="remove item" src='/img/minus.png' />
            </div>
        % endfor
        <div class="section-title">Add here dump junk quantity over-time</div>
        <div class="quantity"> 
            <div class="form-row">
                <label for='qty_start_date'>Start date:</label>
                <input type="text" id="qty-start-date-0" name="qty-start-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='qty_end_date'>End date:</label>
                <input type="text" id="qty-end-date-0" name="qty-end-date-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='type'>Quantity:</label>
                <input type="text" id="qty-0" name="qty-0" value='-1'>
            </div>
            <div class='form-row'>
                <label for='qty-note'>Notes:</label>
                <textarea id='qty-notes-0' name='qty-notes-0'></textarea>
                <div class='notes-counter'></div>
            </div>
            <a href="#" id='qty-addbutton-0' onclick='addQtyField(); return false;'><img class="plus" src="/img/plus.png"></a><br />
        </div>
        <div id="new-qtyfield">
        </div>
        <div class="section-title">Existing CER codes</div>
        % for i in c.cerdump:
            <div id="cer-modview-${i.cd_id}">
                CER code: ${i.cer_code}  Description: ${i.cer_desc} 
                <img onclick="deleteCerDump(${i.cd_id});" class="minus" alt="remove item" src='/img/minus.png' />
            </div>
        % endfor
        <div class="section-title">Add here CER codes for this dump</div>
        <div class="cer">
            <div class="form-row">
                <label for='cer'>CER code:</label>
                <input type="text" id="cer-auto-0" name="cer-auto-0" class="cer-auto" size="45" onfocus="tform=0; doCerCompl();">
                <input type="hidden" name="cer-auto-id-0" id="cer-auto-id-0" value="-1">
            </div>
            <a href="#" id='cer-addbutton-0' onclick='addCerField(); return false;'><img class="plus" src="/img/plus.png"></a><br />
        </div>
        <div id="new-cerfield">
        </div>
        <div class="section-title">Existing biblio for the dump</div>
        % for i in c.bibdump:
            <div id="bib-modview-${i.bd_id}">
                Description: ${i.bd_desc} URL: ${i.bd_url}
                <img onclick="deleteBibDump(${i.bd_id});" class="minus" alt="remove item" src='/img/minus.png' />
            </div>
        % endfor
        <div class="section-title">Add here biblio for this dump</div>
        <div class="bib">
            <div class="form-row">
                <label for='bib'>Bib title:</label>
                <input type="text" id="bib-title-0" name="bib-title-0" size="45">
            </div>
            <div class="form-row">
                <label for='bib'>Bib url:</label>
                <input type="text" id="bib-url-0" name="bib-url-0" size="60">
            </div>
            <div class="form-row">
                <label for='bib'>Bib ref.date:</label>
                <input type="text" id="bib-refdate-0" name="bib-refdate-0" class="datepick">
            </div>
            <div class="form-row">
                <label for='bibtype'>Bib type:</label>
                <select id="bib-type-0" name="bib-type-0">
                    <option value="text">Text</option>
                    <option value="audio">Audio</option>
                    <option value="video">Video</option>
                    <option value="photo">Photo</option>
                </select>
            </div>
            <a href="#" id='bib-addbutton-0' onclick='addBibField(); return false;'><img class="plus" src="/img/plus.png"></a><br />
        </div>
        <div id="new-bibfield">
        </div>
        
        <div class="genbutton">
            ${h.submit('submit','Submit','submitbutton')}
        </div>
    ${h.end_form()}
</div>
