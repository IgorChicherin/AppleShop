from django.core.management.base import BaseCommand
from shop.models import Goods, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        goods = [
            {
                'name': 'MacBook ', 'head': 'MacBook Pro', 'text': 'Раскрывает таланты. <br> С первого касания.',
                'img_lg': 'macbookpro_large.png', 'img_md': '', 'img_sm': 'macbookpro_small.png', 'category_id': '0'
            },
            {
                'name': 'iMac ', 'head': 'iMac',
                'text': 'Retina. Внушительный или колоссальный — <br> выберите свой размер.',
                'img_lg': 'imac_large.png', 'img_md': '', 'img_sm': 'imac_small.png', 'category_id': '0'
            },
            {
                'name': 'Сравните модели ', 'head': 'Сравните модели Mac.',
                'text': '',
                'img_lg': 'compare_large.png', 'img_md': '', 'img_sm': 'compare_small.png', 'category_id': '0'
            },
            {
                'name': 'iPad Pro', 'head': 'iPad Pro', 'text': 'Компьютер. Более чем.<br> В двух размерах.',
                'img_lg': 'ipadpro_large.jpg', 'img_md': 'ipadpro_medium.jpg', 'img_sm': 'ipadpro_small.jpg',
                'category_id': '0'
            },
            {
                'name': 'iPad', 'head': 'iPad', 'text': 'Легко поддержит <br> ваши увлечения.',
                'img_lg': 'ipad_large.jpg', 'img_md': 'ipad_medium.jpg', 'img_sm': 'ipad_small.jpg', 'category_id': '0'
            },
            {
                'name': 'iWatch S2', 'head': 'iWatch', 'text': 'Series 2',
                'img_lg': 'hero_activity_rings_large.jpg', 'img_md': 'hero_activity_rings_medium.jpg',
                'img_sm': 'hero_activity_rings_small.jpg', 'category_id': '0'
            },
            {
                'name': 'iWatch S1', 'head': 'iWatch', 'text': 'Series 1',
                'img_lg': 'series_one_large.jpg', 'img_md': 'series_one_medium.jpg',
                'img_sm': 'series_one_small.jpg', 'category_id': '0'
            }
        ]
        ipads = [

        ]
        iwatchs = [

        ]
        categories = [
            {'name': 'Mac'}, {'name': 'iPad'}, {'name': 'iWatch'}
        ]
        Goods.objects.all().delete()
        for good in goods:
            new_mac = Goods(**good)
            new_mac.save()

        # Ipad.objects.all().delete()
        # for ipad in ipads:
        #     new_ipad = Ipad(**ipad)
        #     new_ipad.save()
        #
        # Iwatch.objects.all().delete()
        # for iwatch in iwatchs:
        #     new_iwatch = Iwatch(**iwatch)
        #     new_iwatch.save()

        Category.objects.all().delete()
        for category in categories:
            new_cat = Category(**category)
            new_cat.save()
