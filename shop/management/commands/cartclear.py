from django.core.management.base import BaseCommand
from shop.models import Cart
from django.utils import timezone


class Command(BaseCommand):
    help = 'Delete not checkout cart\'s'

    def handle(self, *args, **options):
        carts = Cart.objects.filter(created__date__lt=timezone.now(), order__isnull=True)
        count = carts.count()
        carts.delete()
        self.stdout.write(self.style.SUCCESS('Deleted not checkouts carts: %d' % count))