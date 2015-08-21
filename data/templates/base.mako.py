# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1287694616.4868441
_template_filename=u'/var/www/marco@shift-left.net/chroot/disc.sleft.net/disc.sleft.net-html/discariche/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['css_jscript']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/navmenu.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n<html>\n<head>\n    <title></title>\n    ')
        # SOURCE LINE 7
        __M_writer(escape(self.css_jscript()))
        __M_writer(u'\n</head>\n    ')
        # SOURCE LINE 18
        __M_writer(u'\n<body>\n    <div id="container">\n        \n        <div id="navheader">\n            ')
        # SOURCE LINE 23
        __M_writer(escape(self.navheader()))
        __M_writer(u'\n        </div>\n        \n        <div id="content">\n           ')
        # SOURCE LINE 27
        __M_writer(escape(next.body()))
        __M_writer(u'\n        </div>\n        <div id="footer">\n            Discariche in campania\n        </div>\n    </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_jscript(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n        ')
        # SOURCE LINE 10
        __M_writer(escape(h.stylesheet_link('/css/main.css')))
        __M_writer(u'\n        ')
        # SOURCE LINE 11
        __M_writer(escape(h.stylesheet_link('/css/ui-lightness/jquery-ui-1.8.5.custom.css')))
        __M_writer(u'\n        ')
        # SOURCE LINE 12
        __M_writer(escape(h.stylesheet_link('/css/ddmenu.css')))
        __M_writer(u'\n        ')
        # SOURCE LINE 13
        __M_writer(escape(h.javascript_link('/js/jquery-1.4.2.min.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 14
        __M_writer(escape(h.javascript_link('/js/jquery-ui-1.8.5.custom.min.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 15
        __M_writer(escape(h.javascript_link('/js/jquery.validate.min.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 16
        __M_writer(escape(h.javascript_link('/js/jquery.form.js')))
        __M_writer(u'\n        ')
        # SOURCE LINE 17
        __M_writer(escape(h.javascript_link('/js/ddmenu.js')))
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


