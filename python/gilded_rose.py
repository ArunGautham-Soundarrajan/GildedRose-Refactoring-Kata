# -*- coding: utf-8 -*-
from item_handler import (
    NormalItemHandler,
    AgedBrieItemHandler,
    BackstagePassesItemHandler,
    SulfurasItemHandler,
    ConjuredItemHandler,
)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def get_handler(self, item):
        """Returns the correct handler for the item"""
        if item.name == "Aged Brie":
            return AgedBrieItemHandler(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesItemHandler(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItemHandler(item)
        elif item.name.startswith("Conjured"):
            return ConjuredItemHandler(item)
        else:
            return NormalItemHandler(item)

    def update_quality(self):
        """Updates the quality of all items"""
        for item in self.items:
            handler = self.get_handler(item)
            handler.handle_update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
