from django.shortcuts import render_to_response
from django.template import RequestContext
from datatableview.utils import *

# Initialize datatable element
def toffee_get_datatable_structure(ajax_url, options, model=None):
    """
    Uses ``options``, a dict or DatatableOptions, into a ``DatatableStructure`` for template use.

    """

    if not isinstance(options, DatatableOptions):
        options = DatatableOptions(model, {}, **options)
    data_table = DatatableStructure(ajax_url, options, model=model)
    data_table.type = 'datatable'
    return data_table


def toffee_render_to_response(request, content, navbar=None, sidebar=None, footer=None, title="Hello World"):
    #import ipdb; ipdb.set_trace()
    return render_to_response('app_template.html', locals(), context_instance=RequestContext(request))

#class Header(object):
#    '''
#        Adds a new header structure to your project template.
#        Add your css, scripts to /static/ folder and refer to them here
#    '''
#
#    def __init__(self, title):
#        self.title = title
#        self.styles = []
#        self.scripts = []
#        self.metas = {}
#
#    def get_title(self):
#        return self.title
#
#    def get_styles(self):
#        return self.styles
#
#    def get_scripts(self):
#        return self.scripts
#
#    def get_meta(self):
#        return self.metas
#
#    def add_scripts(self, scripts):
#        for script in scripts:
#            self.scripts.append(script)
#
#    def add_styles(self, styles):
#        for style in styles:
#            self.styles.append(style)
#
#    def add_meta(self, metas):
#        for meta_type, meta in metas.iteritems():
#            try:
#                if meta_type == '':
#                    raise ValueError("Meta type can't be empty.")
#                else:
#                    self.metas[meta_type] = meta
#            except ValueError as error:
#                #Log it
#                raise ValueError(error)
#
#    def set_header(self, request, scripts=[], styles=[], metas={}):
#        self.add_scripts(scripts)
#        self.add_styles(styles)
#        self.add_meta(metas)
#        return render(request, 'toffee/base.html',
#                      {'title': self.title, 'styles': self.get_styles(), 'scripts': self.get_scripts(),
#                       'metas': self.get_meta()})
