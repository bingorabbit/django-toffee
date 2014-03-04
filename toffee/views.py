# """For testing"""
# from toffee.utils import toffee_render_to_response, toffee_get_datatable_structure
# from toffee.ui import *
# from toffee.helpers import *
# from django.db.models import Q
# from toffee.models import Countries, Countries2, Mobiles
# #from django_datatables_view.base_datatable_view import BaseDatatableView
# from eztables.views import DatatablesView
# # from datatableview.views import DatatableView
# # from datatableview import helpers
# from django.http import HttpResponse
# import json
# from django.core.serializers.json import DjangoJSONEncoder
# JSON_MIMETYPE = 'application/json'
# # from django.views.generic import TemplateView
# # from django.core.urlresolvers import reverse
# # from datatableview.utils import get_datatable_structure
#
#
# class ContactForm(FormItem):
#     action = ''
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False, label='Your e-mail address')
#     message = forms.CharField(widget=forms.Textarea)
#
#
# class CountriesJsonData(DatatablesView):
#     model = Mobiles
#     fields = (
#         'id',
#         'mobile_model',
#         'mobile_name',
#         'country__country'
#     )
#     # Adding URLs to special column to be able to interpret it..
#     def json_response(self, data):
#         for o in data['aaData']:
#             o[1] = u'<a href="%s">%s</a>' % ("mobiles/"+str(o[0]), o[1])
#         return HttpResponse(
#             json.dumps(data, cls=DjangoJSONEncoder),
#             mimetype=JSON_MIMETYPE
#         )
#
#
# # class EmbeddedTableDatatableView(TemplateView):
# #
# #     def get_template_names(self):
# #         """ Try the view's snake_case name, or else use default simple template. """
# #         name = self.__class__.__name__.replace("DatatableView", "")
# #         return ["demos/" + name.lower() + ".html", "app_template.html"]
# #
# #     def get_context_data(self, **kwargs):
# #         context = super(EmbeddedTableDatatableView, self).get_context_data(**kwargs)
# #
# #         datatable_view = MobilesJsonData()
# #         options = datatable_view.get_datatable_options()
# #         datatable = get_datatable_structure(reverse('countries_data'), options)
# #
# #         context['datatable'] = datatable
# #         return context
# #
# #
# # class MobilesJsonData(DatatableView, DataTableItem):
# #
# #     model = Mobiles
# #     datatable_options = {
# #         'structure_template': 'datatable_template.html',
# #         'columns': [
# #             ('ID', 'id'),
# #             ("Model", 'mobile_model', helpers.link_to_model),
# #             #'mobile_model',
# #             ('Mobile Name', 'mobile_name'),
# #         ],
# #     }
#
#
# # class MobilesJsonData2(DatatablesView):
# #     model = Mobiles
# #     fields = (
# #         'id',
# #         ('mobile_model', helpers.link_to_model),
# #         'mobile_name',
# #         'country__country'
# #     )
#
# # class CountriesJsonData2(BaseDatatableView):
# #     model = Countries2
# #     columns = ['country_code', 'country']
# #     order_columns = ['country_code', 'country']
# #     datatable_options = {
# #         'columns': [
# #             ("Publication date", 'country')
# #         ]
# #     }
# #     def filter_queryset(self, qs):
# #         # sSearch = self.request.GET.get('sSearch', None)
# #         sSearch = dict((k, v) for k, v in self.request.GET.iteritems() if "sSearch" in k)
# #         if sSearch:
# #             filter_query = {"%s__istartswith" % CountriesJsonData.columns[0]: sSearch.pop("sSearch_0"),
# #                             "%s__istartswith" % CountriesJsonData.columns[1]: sSearch.pop("sSearch_1")}
# #             qs = qs.filter(Q(**filter_query))
# #         return qs
#
#
# def index(request):
#     nav_item = NavItem(NavItem.LINK_ITEM)
#     mylink2 = nav_item(link='http://www.google.com', text='google.com')
#     mylink3 = nav_item(link='http://www.yahoo.com', text='yahoo.com')
#     mynav = Navbar([mylink2, mylink3])
#     link = LinkItem(link='http://www.tedata.net.eg', text='tedata.net', active=True)
#     sidebar = Sidebar(children=[link])
#     paragraph = ParagraphItem("Welcome to stage 1", heading="This is Heading")
#     centered_paragraph = ParagraphItem("Welcome to stage 1", alignment="center", heading="Center Aligned Paragraph")
#     # Initialize the datatable
#     # datatable_view = MobilesJsonData()
#     # options = datatable_view.get_datatable_options()
#     # datatable = toffee_get_datatable_structure(reverse('countries_data'), options)
#     datatable = TableItem("countries_data", pagination='full_numbers', fields=CountriesJsonData.fields)
#     print datatable
#     data_table2 = TableItem("countries2_json")
#     paragraph2 = ParagraphItem("Simple footer text")
#     my_form = ContactForm()
#     content = Content(children=[paragraph, datatable, centered_paragraph, my_form])
#     #import ipdb; ipdb.set_trace()
#     footer = Footer(children=[paragraph2])
#     if request.method == "POST":
#         my_form = ContactForm(request.POST)
#         if my_form.is_valid():
#             return toffee_render_to_response(request, navbar=mynav, sidebar=sidebar, content=content, footer=footer,
#                                              title="Form Validated")
#         else:
#             content = Content(children=[paragraph, centered_paragraph, my_form])
#             return toffee_render_to_response(request, navbar=mynav, sidebar=sidebar, content=content, footer=footer,
#                                              title="Form submissions are not valid")
#     return toffee_render_to_response(request, navbar=mynav, sidebar=sidebar, content=content, footer=footer,
#                                      title="Our kick-ass site !!")
#
#
# def index2(request):
#     nav_item = NavItem(NavItem.LINK_ITEM)
#     mylink2 = nav_item(link='http://www.google.com', text='google.com')
#     mylink3 = nav_item(link='http://www.yahoo.com', text='yahoo.com')
#     mynav = Navbar([mylink2, mylink3])
#     link = LinkItem(link='http://www.tedata.net.eg', text='tedata.net', active=True)
#     sidebar = Sidebar(children=[link])
#     paragraph = ParagraphItem("Welcome to stage 1", heading="This is Heading")
#     centered_paragraph = ParagraphItem("Welcome to stage 1", alignment="center", heading="Center Aligned Paragraph")
#     data_table = TableItem("countries2_json", pagination='full_numbers')
#     #data_table2 = TableItem(Countries, ['country_code', 'country'], ['country_code', 'country'])
#     paragraph2 = ParagraphItem("Simple footer text")
#     my_form = ContactForm()
#     content = Content(children=[paragraph, data_table, centered_paragraph, my_form])
#     footer = Footer(children=[paragraph2])
#     if request.method == "POST":
#         my_form = ContactForm(request.POST)
#         if my_form.is_valid():
#             return toffee_render_to_response(request, navbar=mynav, sidebar=sidebar, content=content, footer=footer,
#                                          title="Form Validated")
#         else:
#             content = Content(children=[paragraph, centered_paragraph, my_form])
#             return toffee_render_to_response(request, navbar=mynav, sidebar=sidebar, content=content, footer=footer,
#                                          title="Form submissions are not valid")
#     return toffee_render_to_response(request, navbar=mynav, sidebar=sidebar, content=content, footer=footer,
#                                      title="Our kick-ass site !!")
#
#
# def mobiles(request, mobile_id=None):
#     mobile = Mobiles.objects.get(id=mobile_id)
#     return HttpResponse(mobile.mobile_name)