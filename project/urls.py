from django.conf.urls.defaults import *
from recipes.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),
    (r'^register/$', register),
    (r'^login/$', userlogin),
    (r'^logout/$', userlogout),
    (r'^sarasas/$', sarasas),
    (r'^paieska/$', paieska),
    (r'^kurimas/$', kurimas),
    (r'^kontaktai/$', kontaktai),
    (r'^changepsw/$', changepsw),
    (r'^receptas/(?P<recipe_id>\d+)/$', receptas),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'recipes/images'}),
    (r'^styles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'recipes/styles'}),
)
