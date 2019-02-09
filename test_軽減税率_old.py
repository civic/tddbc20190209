from 軽減税率_old import Food, Liquor, NewsPaper, Beverage, Drug


class Test軽減税率:
    class Test対象の商品:

        def test_食料品(self):
            assert Food("超熟").is_target() == True

        def test_新聞(self):
            assert NewsPaper("毎日").is_target() == True

        def test_清涼飲料水(self):
            assert Beverage("オロナミンC").is_target() == True

    class Test対象外の商品:
        def test_お酒(self):
            assert Liquor("大五郎").is_target() == False
        def test_医薬品(self):
            assert Drug("バファリン").is_target() == False
