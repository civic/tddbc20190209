from 軽減税率 import Product, CategoryOf軽減税率


class Test軽減税率:
    class Test対象の商品:

        def test_食料品(self):
            sut = Product("超熟", CategoryOf軽減税率.Food, 100)

            assert sut.is_reducible() == True

        def test_新聞(self):
            sut = Product("毎日新聞", CategoryOf軽減税率.NewsPaper, 100)

            assert sut.is_reducible() == True

        def test_清涼飲料水(self):
            sut = Product("オロナミンC", CategoryOf軽減税率.Beverage, 100)

            assert sut.is_reducible() == True

    class Test対象外の商品:
        def test_お酒(self):
            sut = Product("大五郎", CategoryOf軽減税率.Liquor, 100)

            assert sut.is_reducible() == False

        def test_医薬品(self):
            sut = Product("バファリン", CategoryOf軽減税率.Drug, 100)

            assert sut.is_reducible() == False

        def test_医薬部外品(self):
            sut = Product("リポビタンD", CategoryOf軽減税率.QuasiDrug, 100)

            assert sut.is_reducible() == False

    class Test税込みの商品合計金額を計算できる:

        def test_単一の商品の合計金額_軽減税率対象(self):
            product = Product("伊右衛門", CategoryOf軽減税率.Beverage, 140)

            assert product.subtotal(1) == 151  # 切り捨て

        def test_単一の商品の合計金額_軽減税率対象外(self):
            product = Product("大五郎", CategoryOf軽減税率.Liquor, 1798)

            assert product.subtotal(1) == 1977  # 切り捨て

        def test_単一カテゴリの複数商品の合計金額_軽減税率対象(self):
            product = Product("伊右衛門", CategoryOf軽減税率.Beverage, 141)

            expected = int((141 * 10) * 1.08)

            assert product.subtotal(10) == expected  # 切り捨て
