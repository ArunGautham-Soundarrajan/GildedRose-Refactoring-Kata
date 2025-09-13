class ItemHandler:
    def __init__(self, item):
        self.item = item
        self.degradation_rate = 1

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_quality(self):
        pass

    def cal_degradation_rate(self):
        if self.item.sell_in <= 0:
            return self.degradation_rate * 2
        return self.degradation_rate

    def handle_update(self):
        self.update_quality()
        self.update_sell_in()


class NormalItemHandler(ItemHandler):
    def update_quality(self):
        self.item.quality = max(0, self.item.quality - self.cal_degradation_rate())
