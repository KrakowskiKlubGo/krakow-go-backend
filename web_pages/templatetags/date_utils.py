from datetime import date, timedelta

from django.template import Library
from django.utils import formats
from django.utils.translation import get_language

register = Library()


@register.simple_tag
def next_wednesday():
    """
    Returns the current or next Wednesday's date, formatted in the active locale.
    - If today is Wednesday, returns today.
    - Otherwise, returns the upcoming Wednesday.
    Format examples:
      Polish:  11 marca 2026
      English: March 11, 2026
    """
    today = date.today()
    # weekday(): Monday=0 ... Wednesday=2 ... Sunday=6
    days_ahead = (2 - today.weekday()) % 7
    wednesday = today + timedelta(days=days_ahead)

    lang = get_language()
    if lang and lang.startswith("pl"):
        MONTHS_PL = [
            "",
            "stycznia",
            "lutego",
            "marca",
            "kwietnia",
            "maja",
            "czerwca",
            "lipca",
            "sierpnia",
            "września",
            "października",
            "listopada",
            "grudnia",
        ]
        return f"{wednesday.day} {MONTHS_PL[wednesday.month]} {wednesday.year}"
    else:
        # Use Django's locale-aware date formatting for other languages
        return formats.date_format(wednesday, format="F j, Y")
