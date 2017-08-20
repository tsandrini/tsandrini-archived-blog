from django.utils.translation import ugettext as _
from django.utils.translation import ungettext as _n

def activate(entityadmin, request, queryset):
    rows_updated = queryset.update(active=True)
    entityadmin.message_user(request, _n(
        'One row was succefully activated',
        '%(count)d rows were succesfully activated',
        rows_updated
    ) % {
        'count': rows_updated
    })
activate.short_description = _("Activate marked rows")
