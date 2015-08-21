<%inherit file="/admin/admin.mako" />
<div class="generic-form">
    <div class="title">View dumps</div>
    % for i in c.dumps:
        <div class="form-row" id="dumpview-${i.id}">
            ${i.name} - <a href="/admin/moddump/${i.id}">Modify</a>
            <img onclick="destroyDump(${i.id});" class="minus" alt="remove item" src='/img/minus.png' />
        </div>
    % endfor
</div>
