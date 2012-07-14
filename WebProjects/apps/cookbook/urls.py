from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "cookbook/index.html"}, name="index"),
    url(r"^login/$", direct_to_template, {"template": "cookbook/login.html"}, name="login"),
)
