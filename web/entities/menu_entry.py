from django.db import models
from django.utils.translation import ugettext as _

class MenuEntry(models.Model):
    slug = models.SlugField(
        _("Slug"),
        # Translators: Slug help text shown in MenuEntry form
        help_text=_("Slug used in URL. Leave blank if creating a parent entry containing multiple other entries")
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        # Translators: Parent help text shown in MenuEntry form
        help_text=_("Parent menu entry (nested list -> eg. dropdown menu)")
    )
    position = models.PositiveIntegerField(
        _("Position"),
        # Translators: Position help text shown in MenuEntry form
        help_text=_("Determines in which order should the entries be drawn")
    )
    enabled = models.BooleanField(
        _("Enabled"),
        default=False,
        # Translators: Enabled help text shown in MenuEntry form
        help_text=_("Disabled entities aren't publicaly available")
    )

    class Meta:
        # Translators: Metadata for MenuEntry entity
        verbose_name = _("Menu entry")
        # Translators: Metadata for MenuEntry entity
        verbose_name_plural = _("Menu entries")

    def __str__(self):
        return "%s [%d:%d]" % (
            self.slug,
            self.parent.id if self.parent != None else 0,
            self.position
        )
