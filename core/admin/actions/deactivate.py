from django.utils.translation import ugettext as _
from django.utils.translation import ungettext as _n

def deactivate(entityadmin, request, queryset):
    rows_updated = queryset.update(active=False)
    entityadmin.message_user(request, _n(
        'One row was succefully deactivated',
        '%(count)d rows were succesfully deactivated',
        rows_updated
    ) % {
        'count': rows_updated
    })
deactivate.short_description = _("Deactivate marked rows")
