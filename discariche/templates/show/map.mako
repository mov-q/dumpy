<%inherit file="/show/show.mako" />
<div id="show-left">
    <div id="show-map">
    </div>
    <div id="show-info">
        <div id="card-position">
            <div class="info-title">Posizione</div>
            <div class="info-entry">
                <div class="info-item">Latitudine:</div> <div id="latitude"></div>
            </div>
            <div class="info-entry">
                <div class="info-item">Longitudine:</div> <div id="longitude"></div>
            </div>
            <div class="info-title">Destinazioni</div>
            <div id="dest"></div>
            <div class="info-title">Status</div>
            <div id="status"></div>
            <div class="info-title">Quantità</div>
            <div id="qty"></div>
            <div class="info-title">Proprietà</div>
            <div id="agent"></div>
        </div>
    </div>
</div>
<div id="show-right">
    <div id="card-title">
    </div>
    <div id="card-subtitle">
    </div>
    <div id="card-history">
    </div>
</div>
<script type="text/javascript">
    initialize();
</script>
