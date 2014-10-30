from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orcamentofacil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'orcamentos.views.base', name='base'),
    url(r'^cadastros/$', 'cadastros.views.cadastros', name='cadastros'),
    # url(r'^edit/$', 'cadastros.views.edit_produtos', name='edit_produtos'),
    url(r'^members/(?P<username>\w+)/$', 'cadastros.views.add_produtos', name='add_produtos'),
    url(r'^cadastros/produto/(?P<id>\d+)/$', 'cadastros.views.delete_produtos', name='delete_produtos'),
    url(r'^cadastros/client/(?P<id>\d+)/$', 'cadastros.views.delete_clients', name='delete_clients'),
    url(r'^cadastros/shipping/(?P<id>\d+)/$', 'cadastros.views.delete_shippings', name='delete_shippings'),
    url(r'^single_produto/(?P<id>.*)/$', 'cadastros.views.edit_produtos', name='edit_produtos'),
    url(r'^edit_clients/(?P<id>.*)/$', 'cadastros.views.edit_clients', name='edit_clients'),
    url(r'^add_clients/$', 'cadastros.views.add_clients', name='add_clients'),
    url(r'^add_shippings/$', 'cadastros.views.add_shippings', name='add_shippings'),
    url(r'^edit_shippings/(?P<id>.*)/$', 'cadastros.views.edit_shippings', name='edit_shippings'),
    url(r'^add_service/$', 'cadastros.views.add_services', name='add_services'),
    url(r'^add_garantia/$', 'cadastros.views.add_garantia', name='add_garantia'),
    url(r'^add_terms/$', 'cadastros.views.add_terms', name='add_terms'),
    # url(r'^add_productshippings/$', 'cadastros.views.add_productshippings', name='add_productshippings'),
    # url(r'^members/(?P<username>\w+)/$', 'cadastros.views.produto_table', name='produto_table'),
    # url(r'^$', 'orcamentos.views.navbar', name='navbar'),
    (r'^accounts/', include('registration.urls')),
    # url(r'^people/$', 'cadastros.views.people', name='people'),
)
