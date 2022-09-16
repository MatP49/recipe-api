from django.core.management.base import BaseCommand
import time 
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('waiting for database....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write('Database unavalaible')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("DB available !"))
