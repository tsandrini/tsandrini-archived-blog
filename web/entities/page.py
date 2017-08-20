from django.db import models
from django.utils.translation import ugettext as _

class Page(models.Model):
    identifier = models.CharField(
        _("Identifier"),
        max_length=50,
        # Translators: Identifier help text shown in Page form
        help_text=_("Unique page identifier. Used if target page is going to be static for template loading and other unique situtations")
    )
    content = models.TextField(
        _("Content"),
        null=True,
        # Translators: Content help text shown in Page form
        help_text=_("Template content. Django template syntax is supported")
    )
    dynamic_content = models.BooleanField(
        _("Dynamic content"),
        default=True,
        # Translators: Dynamic content help text shown in Page form
        help_text=_("Determines, whether the page is loaded from a database storage or from a static template")
    )
    template_path = models.CharField(
        _("Template path"),
        max_length=155,
        null=True,
        # Translators: Template path help text shown in Page form
        help_text=_("Template path for static handled pages")
    )
    dynamic_handling = models.BooleanField(
        _("Dynamic handling"),
        default=False,
        # Translators: Dynamic handling help text shown in Page form
        help_text=_("Determines, whether the page owns a self handling action method")
    )
    active = models.BooleanField(
        _("Active"),
        default=True,
        # Translators: Active help text shown in Page form
        help_text=_("Non active pages won't be shown")
    )

    class Meta:
        # Translators: Metadata for Page entity
        verbose_name = _("Page")
        # Translators: Metadata for Page entity
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.identifier
