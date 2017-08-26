from django.utils.translation import ugettext as _
from django.utils.translation import ungettext as _n

def enable(entityadmin, request, queryset):
    rows_updated = queryset.update(enabled=True)
    entityadmin.message_user(request, _n(
        'One row was succefully enabled',
        '%(count)d rows were succesfully enabled',
        rows_updated
    ) % {
        'count': rows_updated
    })
enable.short_description = _("Enable marked rows")
