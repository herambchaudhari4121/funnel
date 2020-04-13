# -*- coding: utf-8 -*-

from baseframe import __
from coaster.utils import nullint
import baseframe.forms as forms

__all__ = ['SavedSessionForm', 'SessionForm']


class SessionForm(forms.Form):
    title = forms.StringField(
        __("Title"),
        validators=[forms.validators.DataRequired()],
        filters=[forms.filters.strip()],
    )
    venue_room_id = forms.SelectField(
        __("Room"), choices=[], coerce=nullint, validators=[forms.validators.Optional()]
    )
    description = forms.MarkdownField(
        __("Description"), validators=[forms.validators.Optional()]
    )
    speaker = forms.StringField(
        __("Speaker"),
        validators=[forms.validators.Optional(), forms.validators.Length(max=200)],
        filters=[forms.filters.strip()],
    )
    speaker_bio = forms.MarkdownField(
        __("Speaker bio"), validators=[forms.validators.Optional()]
    )
    banner_image_url = forms.URLField(
        __("Banner image URL"),
        description="Banner image for session card",
        validators=[
            forms.validators.Optional(),
            forms.validators.ValidUrl(),
            forms.validators.Length(max=2000),
        ],
    )
    is_break = forms.BooleanField(__("This session is a break period"), default=False)
    featured = forms.BooleanField(__("This is a featured session"), default=False)
    start_at = forms.HiddenField(
        __("Start Time"), validators=[forms.validators.DataRequired()]
    )
    end_at = forms.HiddenField(
        __("End Time"), validators=[forms.validators.DataRequired()]
    )


class SavedSessionForm(forms.Form):
    save = forms.BooleanField(
        __("Save this session?"), validators=[forms.validators.InputRequired()]
    )
    description = forms.StringField(__("Note to self"))
