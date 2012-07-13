from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from mysite.liga.sitemap import TeamSitemap, TableResultsSitemap, PlayerSitemap, StaticSitemap

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"

sitemaps={
  "team":TeamSitemap,
  "tableresults":TableResultsSitemap,
  "player":PlayerSitemap,
  "static":StaticSitemap,
}

urlpatterns = patterns("",
    #url(r"^$", direct_to_template, {
    #    "template": "homepage.html",
    #}, name="home"),
    url(r"^$", include("liga.urls")),
    url(r"^tabela/$", direct_to_template, {"template": "tabela.html"}, name="tabela"),
    url(r"^profil/(?P<tag>\w+)$", 'mysite.liga.views.manage_profil'),
    url(r"^tabela/pdf$", 'mysite.liga.views.create_pdf'),
    url(r"^druzyny$", 'mysite.liga.views.manage_team'),
    url(r"^mecze/(?P<tag>\w+)$", 'mysite.liga.views.manage_match'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
