from django.contrib.sitemaps import Sitemap
from mysite.liga.models import Player, TableResults, Team
import datetime
import os

from django.contrib import sitemaps
from django.core import urlresolvers
from django.conf import settings


class AbstractSitemapClass():
    url = None
    def get_absolute_url(self):
        return self.url

class StaticSitemap(Sitemap):
        pages = {
             'home':'/',
             'account_login':'/account/login',
             'account_signup':'/account/signup',
             'account_email':'/account/email',
             'account_password_change':'/account/password_change',
             'account_avatar_change':'/account/avatar',
             'admin':'/admin',
        }
        main_sitemaps = []
        for page in pages.keys():
                sitemap_class = AbstractSitemapClass()
                sitemap_class.url = pages[page]        
                main_sitemaps.append(sitemap_class)

        priority = 0.4
        changefreq = "yearly"  
        def items(self):
                return self.main_sitemaps    
        def lastmod(self, obj):
                return datetime.datetime(2012, 1, 5)
        
class TeamSitemap(Sitemap):
        priority = 0.7
        changefreq = "monthly"  
        def items(self):
                return Team.objects.all()
        def lastmod(self, obj):
                return datetime.datetime(2012, 1, 5)


class TableResultsSitemap(Sitemap):
        priority = 0.4
        changefreq = "monthly"  
        def items(self):
                return TableResults.objects.all()
        def lastmod(self, obj):
                return datetime.datetime(2012, 1, 5)


class PlayerSitemap(Sitemap):
        priority = 0.5
        changefreq = "monthly"  
        def items(self):
                return TableResults.objects.all()
        def lastmod(self, obj):
                return datetime.datetime(2012, 1, 5)



