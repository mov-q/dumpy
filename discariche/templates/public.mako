<%inherit file="/u-menu.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
<head>
    <title></title>
    ${self.css_jscript()}
</head>
    <%def name="css_jscript()">
        ${h.stylesheet_link('/css/public.css')}
        ${h.stylesheet_link('/css/ui-lightness/jquery-ui-1.8.5.custom.css')}
        ${h.javascript_link('/js/jquery-1.4.2.min.js')}
        ${h.javascript_link('/js/jquery-ui-1.8.5.custom.min.js')}
        ${h.javascript_link('/js/jquery.smoothDivScroll-1.1-min.js')}
        ${h.javascript_link('/js/jquery.pagination.js')}
        ${h.javascript_link('/js/jquery.validate.min.js')}
        ${h.javascript_link('/js/jquery.form.js')}
    </%def>
<body>
    <div id="container">
        <div id="header">
        </div>
        <div id="navheader">
            ${self.umenu()}
        </div>
        
        <div id="content">
           ${next.body()}
        </div>
        <div id="footer">
            Discariche in campania
        </div>
    </div>
</body>
</html>
