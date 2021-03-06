from django.core.management.base import BaseCommand, CommandError
from django.db import models
from short_url.models import url_mapping, deleted_url, url_stats
import datetime
import time


class Command(BaseCommand):
    help = 'Command to do........'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            time_up = datetime.datetime.today()
            time_update = int(time.mktime(time_up.timetuple()))
            query_set = url_mapping.objects.all()
            stats_query = url_stats.objects.all()
            stats_const = 1.0
            for obj in query_set:
                time_added=int(obj.added)
                print(time_added)
                timediff=float((time_update-time_added)/2592000)
                print(timediff)
                ttl_month=float(obj.ttl)
                if obj.ttl==-1:
                    pass
                elif timediff > ttl_month:
                    #entry=url_mapping.objects.get(short_url=obj.short_url)
                    deleted_url_instance = deleted_url(deleted_entry=obj.short_url)
                    deleted_url_instance.save()
                    url_mapping.objects.filter(short_url=obj.short_url).delete()
            for code_obj in stats_query:
                hit_time = int (code_obj.hit_time)
                print(hit_time)
                del_time = float((time_update-hit_time)/2592000)
                if del_time > stats_const:
                    url_stats.objects.filter(short_url=code_obj.short_url).delete()



        except Exception as e:
            CommandError(repr(e))