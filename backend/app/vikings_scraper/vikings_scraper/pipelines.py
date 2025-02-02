from scrapy.exceptions import DropItem

from tv_series.models import Norseman, Viking, NFLPlayer
from tv_series.services import VikingService, NFLPlayerService, NorsemanService


class VikingsScraperPipeline:

    def __init__(self):
        self.norseman_service = NorsemanService()
        self.viking_service = VikingService()
        self.nflplayer_service = NFLPlayerService() # TODO:

    def process_item(self, item, spider):
        if spider.name == 'vikings':
            # Existing logic for the 'vikings' spider
            Viking.objects.update_or_create(
                name=item['name'],
                defaults={
                    'actor_name': item.get('actor', ''),
                    'description': item.get('description', ''),
                    'photo': item.get('photo', ''),
                }
            )
        elif spider.name == 'norsemen':
            # Existing logic for the 'norsemen' spider
            Norseman.objects.update_or_create(
                name=item['name'],
                defaults={
                    'actor_name': item.get('actor', ''),
                    'description': item.get('description', ''),
                    'photo': item.get('photo', ''),
                }
            )
        elif spider.name == 'nflplayers':
            # Logic for 'nflplayers' spider
            NFLPlayer.objects.update_or_create(
                name=item['name'],
                defaults={
                    'position': item.get('position', ''),
                    'height': item.get('height', ''),
                    'weight': item.get('weight', ''),
                    'age': item.get('age', None),
                    'experience': item.get('experience', None),
                    'college': item.get('college', ''),
                    'photo_url': item.get('photo_url', ''),  # Save the photo URL
                }
            )
        else:
            raise DropItem(f"Unknown spider: {spider.name}")

        return item
