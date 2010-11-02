"""

Django Celery Event Metadata persister.

"""
from celery.bin import celeryev

from djcelery.management.base import CeleryCommand

camera = celeryev.EvCommand()


class Command(CeleryCommand):
    """Run the celery djcelery event metadata persister."""
    help = 'Takes snapshots of the clusters state to the database.'
    requires_model_validation = True
    option_list = CeleryCommand.option_list + camera.get_options()

    def handle(self, *args, **options):
        options["camera"] = "djcelery.snapshot.Camera"
        camera.run(*args, **options)
