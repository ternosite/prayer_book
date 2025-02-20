from django.contrib.sitemaps import Sitemap
from cal.models import Holiday
from psalms.models import Psalm
from texty.models import Prayer

class HolidaySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Holiday.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class PsalmSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Psalm.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class PrayerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Prayer.objects.all()

sitemaps = {
    'holidays': HolidaySitemap(),
    'psalms': PsalmSitemap(),
    'prayers': PrayerSitemap(),
}
