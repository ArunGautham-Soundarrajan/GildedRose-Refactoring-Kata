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

    def update_quality(self):
        for item in self.items:

            if item.name == "Aged Brie":
                AgedBrieItemHandler(item).handle_update()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                BackstagePassesItemHandler(item).handle_update()
            elif item.name == "Sulfuras, Hand of Ragnaros":
                SulfurasItemHandler(item).handle_update()
            elif item.name.startswith("Conjured"):
                ConjuredItemHandler(item).handle_update()
            else:
                NormalItemHandler(item).handle_update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
