# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_never_negative(self):
        items = [Item("foo", 0, 0), Item("foo", 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[1].quality)

    def test_quality_never_over_50(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_decreases_twice_as_fast(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)


class GildedRoseAgedBrieTest(unittest.TestCase):
    def test_quality_never_over_50(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_increase(self):
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)


class GildedRoseSulfurasTest(unittest.TestCase):
    def test_quality_never_over_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sell_in_never_decrease(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)


class GildedRoseBackstagePassesTest(unittest.TestCase):
    def test_quality_increase(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(22, items[1].quality)
        self.assertEqual(23, items[2].quality)

    def test_quality_drops_to_zero(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", -1, 20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[1].quality)


class GildedRoseConjuredTest(unittest.TestCase):
    def test_quality_decreases_twice_as_fast(self):
        items = [Item("Conjured", 2, 10), Item("Conjured Cake", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(1, items[1].quality)


if __name__ == "__main__":
    unittest.main()
