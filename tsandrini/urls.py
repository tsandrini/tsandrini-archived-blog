from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'tinymce/', include('tinymce.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^', include('web.urls')),
    url(r'^admin/', admin.site.urls),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
