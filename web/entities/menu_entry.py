from django.db import models
from django.utils.translation import ugettext as _

class MenuEntry(models.Model):
    slug = models.SlugField(
        _("Slug")
    )

    class Meta:
        verbose_name = _("Menu entry")
        verbose_name_plural = _("Menu entries")

