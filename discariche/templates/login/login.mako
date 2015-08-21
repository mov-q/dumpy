<%inherit file="/base.mako" />
<%def name="css_jscript()">
    ${parent.css_jscript()}
    ${h.javascript_link('/js/testctr.js')}
</%def>
${next.body()}
