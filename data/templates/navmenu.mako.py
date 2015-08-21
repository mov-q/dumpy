# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1286659867.242954
_template_filename=u'/var/www/marco@shift-left.net/chroot/disc.sleft.net/disc.sleft.net-html/discariche/templates/navmenu.mako'
_template_uri=u'/navmenu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['navheader']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 20
        __M_writer(escape(next.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navheader(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <ul class="tabs">\n        <li><a href="/admin">Home</a></li>\n        <li><a href="/admin/viewdump">Edit/Modify</a>\n            <ul class="dropdown">\n                <li><a href="/insertdata/comune">Comuni</a></li>\n                <li><a href="/insertdata/statoestero">Stati esteri</a></li>\n                <li><a href="/insertdata/prestazione">Prestazione</a></li>\n                <li><a href="/insertdata/esenzione">Esenzioni</a></li>\n                <li><a href="/insertdata/tipomedico">Tipi medico</a></li>\n                <li><a href="/insertdata/onereprestazione">Oneri prestazione</a></li>\n                <li><a href="/insertdata/asl">ASL</a></li>\n                <li><a href="/insertdata/distretto">Distretti</a></li>\n                <!--<li><a href="/insertdata/"></a></li>-->\n            </ul>\n        </li>\n    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


