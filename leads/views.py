from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext




LANGUAGES = (
    ("he", gettext("Hebrew")),
    ("ru", gettext("Russian")),
    ("en", gettext("English")),
    ("ar", gettext("Arabic")),

)

# Create your views here.
def home(request):
    trans = transtate(language="he")
    return render(request, "home.html", {"trans": trans})

def transtate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext("Hello")
    finally:
        activate(cur_language)
    return text