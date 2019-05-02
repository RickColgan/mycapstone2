from django.contrib import admin
from .models import School, Athletes, Scoring, Events, TeamScores, \
    PrelimRaces, FinalRaces

# Register your models here.
# This makes these tables available from the admin site
admin.site.register(School)
admin.site.register(Athletes)
admin.site.register(Scoring)
admin.site.register(Events)
admin.site.register(TeamScores)
admin.site.register(PrelimRaces)
admin.site.register(FinalRaces)