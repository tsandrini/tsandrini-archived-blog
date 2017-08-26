from django.utils.translation import ugettext as _
from django.utils.translation import ungettext as _n

def disable(entityadmin, request, queryset):
    rows_updated = queryset.update(enabled=False)
    entityadmin.message_user(request, _n(
        'One row was succefully disabled',
        '%(count)d rows were succesfully disabled',
        rows_updated
    ) % {
        'count': rows_updated
    })
disable.short_description = _("Disable marked rows")
