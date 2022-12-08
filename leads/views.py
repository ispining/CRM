import os

from django.shortcuts import render
from django.utils.translation import gettext as _




LANGUAGES = (
    ("he", _("Hebrew")),
    ("ru", _("Russian")),
    ("en", _("English")),
    ("ar", _("Arabic")),

)





def home(request):
    trans = translate(language="ru")
    return render(request, "home.html", {"trans": trans})


def translate(language):
    from django.utils.translation import get_language, activate, gettext

    cur_language = get_language()
    print(cur_language)
    try:
        activate(language)
        text = gettext("Hello")
    finally:
        activate(cur_language)
    return text