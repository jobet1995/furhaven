"""
Django management command to wait for the database to be available.
"""
import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Handle the command."""
        self.stdout.write('Waiting for database...')
        db_conn = None
        max_retries = 30
        retry_delay = 1  # seconds

        for attempt in range(max_retries):
            try:
                # Try to connect to the database
                db_conn = connections['default']
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS('Database is available!'))
                return
            except OperationalError as e:
                if attempt < max_retries - 1:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Database unavailable, waiting {retry_delay} second(s)... '
                            f'({attempt + 1}/{max_retries})'
                        )
                    )
                    time.sleep(retry_delay)
                    # Increase delay for next attempt (exponential backoff)
                    retry_delay = min(retry_delay * 2, 10)  # Cap at 10 seconds
                else:
                    self.stderr.write(
                        self.style.ERROR('Database is still not available after maximum retries.')
                    )
                    raise e
