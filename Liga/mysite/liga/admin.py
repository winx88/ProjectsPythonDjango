from django.db import models
from django.contrib import admin
from mysite.liga.models import Player, Team, TableResults, FootballPitch, MatchesResults

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(TableResults)
admin.site.register(FootballPitch)
admin.site.register(MatchesResults)
