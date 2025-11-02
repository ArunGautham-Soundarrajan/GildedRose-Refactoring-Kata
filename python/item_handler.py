class ItemHandler:
    """Base class for item handlers"""

    def __init__(self, item):
        self.item = item
        self.degradation_rate = 1

    def update_sell_in(self):
        """Updates the sell_in value of the item"""
        self.item.sell_in -= 1

    def update_quality(self):
        """Updates the quality value of the item"""
        pass

    def cal_degradation_rate(self):
        """Calculates the degradation rate of the item"""
        if self.item.sell_in <= 0:
            return self.degradation_rate * 2
        return self.degradation_rate

    def handle_update(self):
        """Updates the quality and sell_in values of the item"""
        self.update_quality()
        self.update_sell_in()


class NormalItemHandler(ItemHandler):
    """Normal item handler"""

    def update_quality(self):
        self.item.quality = max(0, self.item.quality - self.cal_degradation_rate())


class AgedBrieItemHandler(ItemHandler):
    """Aged Brie item handler"""

    def update_quality(self):
        self.item.quality = min(50, self.item.quality + self.cal_degradation_rate())


class BackstagePassesItemHandler(ItemHandler):
    """Backstage passes item handler"""

    def cal_degradation_rate(self):
        if self.item.sell_in <= 0:
            return 0
        elif self.item.sell_in <= 5:
            return 3
        elif self.item.sell_in <= 10:
            return 2
        else:
            return 1

    def update_quality(self):
        if self.item.sell_in <= 0:
            self.item.quality = 0
        else:
            self.item.quality = min(50, self.item.quality + self.cal_degradation_rate())


class SulfurasItemHandler(ItemHandler):
    """Sulfuras item handler"""

    def update_quality(self):
        pass

    def update_sell_in(self):
        pass


class ConjuredItemHandler(ItemHandler):
    """Conjured item handler"""

    def cal_degradation_rate(self):
        return self.degradation_rate * 2

    def update_quality(self):
        self.item.quality = max(0, self.item.quality - self.cal_degradation_rate())
