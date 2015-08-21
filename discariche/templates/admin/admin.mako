<%inherit file="/base.mako" />
<%def name="css_jscript()">
    ${parent.css_jscript()}
    ${h.javascript_link('/js/admin.js')}
    ${h.javascript_link('/js/addstatus.js')}
    ${h.javascript_link('/js/addagent.js')}
    ${h.javascript_link('/js/adddt.js')}
    ${h.javascript_link('/js/adddump.js')}
    ${h.javascript_link('/js/moddump.js')}
</%def>
${next.body()}
<div id="resbox">
</div>
