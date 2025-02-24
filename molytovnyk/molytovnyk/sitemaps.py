from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from psalms.models import Psalm
from texty.models import Prayer

class PsalmSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Psalm.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


class PrayerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Prayer.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()



sitemaps = {
    'psalms': PsalmSitemap(),
    'texty': PrayerSitemap(),
}
