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
    url(r'^members/(?P<username>\w+)/$', 'cadastros.views.edit_produtos', name='edit_produtos'),
    # url(r'^$', 'orcamentos.views.navbar', name='navbar'),
    (r'^accounts/', include('registration.urls')),
)
