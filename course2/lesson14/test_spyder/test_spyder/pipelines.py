# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker
from test_spyder.models import Channels, db_connect, create_channel_table

class YtscraperPipeline(object):

    def __init__(self):
        #Initializes database connection and sessionmaker.
        engine = db_connect()
        create_channel_table(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def process_item(self, item, spider):
        # check if item with this title exists in DB
        item_exists = self.session.query(Channels).filter_by(author=item['author']).first()
        # if item exists in DB - we just update 'date' and 'subs' columns.
        if item_exists:
            item_exists.date = item['date']
            item_exists.subs = item['subs'] 
            print('Item {} updated.'.format(item['author']))
        # if not - we insert new item to DB
        else:     
            new_item = Channels(**item)
            self.session.add(new_item)
            print('New item {} added to DB.'.format(item['author']))
        return item    

    def close_spider(self, spider):
        # We commit and save all items to DB when spider finished scraping.
        try:
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()