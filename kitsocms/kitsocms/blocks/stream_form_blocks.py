from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks

from kitsocms.wagtail_flexible_forms import blocks as form_blocks
from kitsocms.blocks.base_blocks import BaseBlock, KitsoAdvSettings
from kitsocms.forms import (
    KitsoDateField, KitsoDateInput,
    KitsoDateTimeField, KitsoDateTimeInput,
    KitsoTimeField, KitsoTimeInput,
    SecureFileField
)


class KitsoFormAdvSettings(KitsoAdvSettings):

    condition_trigger_id = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_('Condition Trigger ID'),
        help_text=_(
            'The "Custom ID" of another field that that will trigger this field to be shown/hidden.')  # noqa
    )
    condition_trigger_value = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_('Condition Trigger Value'),
        help_text=_(
            'The value of the field in "Condition Trigger ID" that will trigger this field to be shown.')  # noqa
    )


class FormBlockMixin(BaseBlock):
    class Meta:
        abstract = True

    advsettings_class = KitsoFormAdvSettings


class KitsoStreamFormFieldBlock(form_blocks.OptionalFormFieldBlock, FormBlockMixin):
    pass


class KitsoStreamFormCharFieldBlock(form_blocks.CharFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Text or Email input")
        icon = "fa-window-minimize"


class KitsoStreamFormTextFieldBlock(form_blocks.TextFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Multi-line text")
        icon = "fa-align-left"


class KitsoStreamFormNumberFieldBlock(form_blocks.NumberFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Numbers only")
        icon = "fa-hashtag"


class KitsoStreamFormCheckboxFieldBlock(form_blocks.CheckboxFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Single Checkbox")
        icon = "fa-check-square-o"


class KitsoStreamFormRadioButtonsFieldBlock(form_blocks.RadioButtonsFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Radios")
        icon = "fa-list-ul"


class KitsoStreamFormDropdownFieldBlock(form_blocks.DropdownFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Dropdown")
        icon = "fa-list-alt"


class KitsoStreamFormCheckboxesFieldBlock(form_blocks.CheckboxesFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Checkboxes")
        icon = "fa-list-ul"


class KitsoStreamFormDateFieldBlock(form_blocks.DateFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Date")
        icon = "fa-calendar"

    field_class = KitsoDateField
    widget = KitsoDateInput


class KitsoStreamFormTimeFieldBlock(form_blocks.TimeFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Time")
        icon = "fa-clock-o"

    field_class = KitsoTimeField
    widget = KitsoTimeInput


class KitsoStreamFormDateTimeFieldBlock(form_blocks.DateTimeFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Date and Time")
        icon = "fa-calendar"

    field_class = KitsoDateTimeField
    widget = KitsoDateTimeInput


class KitsoStreamFormImageFieldBlock(form_blocks.ImageFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Image Upload")
        icon = "fa-picture-o"


class KitsoStreamFormFileFieldBlock(form_blocks.FileFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Secure File Upload")
        icon = "fa-upload"

    field_class = SecureFileField


class KitsoStreamFormStepBlock(form_blocks.FormStepBlock):
    form_fields = blocks.StreamBlock()

    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(
            local_blocks=[
                ('form_fields', blocks.StreamBlock(local_blocks))
            ]
        )
