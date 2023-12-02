# -*- coding: utf-8 -*-

from extension import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_number = db.Column(db.String(255), nullable=False)
    book_name = db.Column(db.String(255), nullable=False)
    book_type = db.Column(db.String(255), nullable=False)
    book_prize = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(255))
    book_publisher = db.Column(db.String(255))

    @staticmethod
    def init_db():
        rets = [
            (1, '001', '活着', '小说', 39.9, '余华', '某某出版社'),
            (2, '002', '三体', '科幻', 99.8, '刘慈欣', '重庆出版社')
        ]
        for ret in rets:
            book = Book()
            book.id = ret[0]
            book.book_number = ret[1]
            book.book_name = ret[2]
            book.book_type = ret[3]
            book.book_prize = ret[4]
            book.author = ret[5]
            book.book_publisher = ret[6]
            db.session.add(book)
        db.session.commit()

class Food(db.Model):
    __tablename__ = 'food'
    fid = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer, db.ForeignKey('ftype.tid'))
    fname = db.Column(db.String(255), nullable=False)
    fpic = db.Column(db.String(255), nullable=False)
    fprice = db.Column(db.Integer, nullable=False)
    forder = db.Column(db.Integer)
    fdesc = db.Column(db.String(500), nullable=False)
    fregtime = db.Column(db.Date, nullable=False)

    ftype = db.relationship('FType', backref=db.backref('foods', lazy=True))

    @staticmethod
    def init_db():
        foods = [
            # Food(fid=1, tid=1, fname='炖豆角', fpic='url_to_image', fprice=25, forder=1, fdesc='美味的炖豆角', fregtime=datetime.now()),
            Food(fid=1, tid=32, fname='虾皮萝卜丝汤',
                 fpic='http://web-final.oss-cn-beijing.aliyuncs.com/foods/52da1ae8a9375.jpg', fprice=14, forder=0,
                 fdesc='清淡的虾皮萝卜丝汤!作为最流行的夏季汤品，逐渐走入大家的心中。清淡的萝卜丝配上淡味的虾皮，将百煮的浓汤浇在汤面上，一碗清淡爽口的虾皮萝卜丝汤出锅了',
                 fregtime=datetime.now()),
            Food(fid=2, tid=32, fname='白蛤蒸蛋',
                 fpic='http://web-final.oss-cn-beijing.aliyuncs.com/foods/52da147fc29fb.jpg', fprice=15, forder=2,
                 fdesc='白蛤蒸蛋　洗净的白蛤经过腌制，放入到新鲜的鸡蛋中，加上各种调味品。海鲜加鸡蛋，不仅美味而且营养价值高，对于害怕海鲜腥味的朋友也可以品尝。',
                 fregtime=datetime.now()),
            Food(fid=3, tid=26, fname='梅子茶泡饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52da0feb79de3.jpg', fprice=10, forder=5,
                 fdesc='梅子茶泡饭 喜欢饭泡水的朋友，一定不能错过，汤水微有酸甜味，米饭软硬适中，是快速餐饮，解饿充饥的首选',
                 fregtime=datetime.now()),
            Food(fid=4, tid=15, fname='水煮肉片',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52da0e14dce6a.jpg', fprice=30, forder=4,
                 fdesc='水煮肉片 使用小米辣椒，辣而不辛，肉片爽滑，轻嚼即化，不油腻，爱吃辣的朋友绝对不能错过',
                 fregtime=datetime.now()),
            Food(fid=5, tid=15, fname='香酥小肉丸',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fcef7a7ab06.jpg', fprice=20, forder=2,
                 fdesc='香酥小肉丸  不油腻，外层酥脆，内层肉质松软', fregtime=datetime.now()),
            Food(fid=6, tid=38, fname='蓝莓味冰激凌',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52da0a1841e10.jpg', fprice=5, forder=1,
                 fdesc='蓝莓味冰激凌  细细的沙冰上面，浇上酸甜可口的蓝莓糖浆，大大的一杯，清凉爽口，是夏季解暑的上佳单品。',
                 fregtime=datetime.now()),
            Food(fid=7, tid=33, fname='酸辣白菜粉丝',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52da1b7bbfe87.jpg', fprice=9, forder=1,
                 fdesc='酸辣白菜粉丝  喜欢吃酸的朋友绝对喜欢这道菜，使用传统手法腌制的酸菜，配上爽口的粉丝，将酸爽融为一体，加上少许的辣椒后，酸中微微带辣，绝对够味',
                 fregtime=datetime.now()),
            Food(fid=8, tid=33, fname='香辣牛肉面',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52da1db1dd3b6.jpg', fprice=8, forder=10,
                 fdesc='香辣牛肉面  麻辣鲜香集为一体，各种调味品加以烹饪，面质劲道，汤味鲜辣，加上爽滑牛肉，就是这个味儿。',
                 fregtime=datetime.now()),
            Food(fid=9, tid=40, fname='苹果橙汁',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fceb99d6f92.jpg', fprice=5, forder=1,
                 fdesc='新鲜的苹果和橙子，现榨现送。', fregtime=datetime.now()),
            Food(fid=10, tid=14, fname='冰爽柠檬汁',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc1e482e4e2.jpg', fprice=6, forder=1,
                 fdesc='温馨雅室正阳春，宾至如归笑语频。 冷气舒身身解暑，热茶润口口生津。 兰芽雀舌今之贵，凤饼龙团古所珍。 绿韵悠悠今胜古，香茗似酒醉游人。',
                 fregtime=datetime.now()),
            Food(fid=11, tid=14, fname='冰镇青柠苏打水',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc1e9874cec.jpg', fprice=4, forder=1,
                 fdesc='温馨雅室正阳春，宾至如归笑语频。 冷气舒身身解暑，热茶润口口生津。 兰芽雀舌今之贵，凤饼龙团古所珍。 绿韵悠悠今胜古，香茗似酒醉游人。',
                 fregtime=datetime.now()),
            Food(fid=12, tid=25, fname='酸妞面包',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fced755d4a1.jpg', fprice=8, forder=1,
                 fdesc='酸妞面包  甜甜的面包，加上少许的酸粉，是早餐、开胃的甜点佳品', fregtime=datetime.now()),
            Food(fid=13, tid=43, fname='拉罐汽水',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc1fea98afd.jpg', fprice=5, forder=1,
                 fdesc='细雨斜风作小寒，  淡烟疏柳媚晴滩.  入淮清洛渐漫漫，  雪沫乳花浮午盏. 蓼茸蒿笋试春盘, 人间有味是清欢.',
                 fregtime=datetime.now()),
            Food(fid=14, tid=32, fname='四物番鸭汤',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fcee55f24eb.jpg', fprice=10, forder=1,
                 fdesc='四物番鸭汤  是美容滋补的上好单品', fregtime=datetime.now()),
            Food(fid=15, tid=40, fname='鲜榨草莓汁',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc206e27500.jpg', fprice=6, forder=1,
                 fdesc='细雨斜风作小寒，  淡烟疏柳媚晴滩.  入淮清洛渐漫漫，  雪沫乳花浮午盏. 蓼茸蒿笋试春盘, 人间有味是清欢.',
                 fregtime=datetime.now()),
            Food(fid=16, tid=40, fname='鲜榨木瓜奶',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc20a9458c6.jpg', fprice=6, forder=1,
                 fdesc='细雨斜风作小寒，  淡烟疏柳媚晴滩.  入淮清洛渐漫漫，  雪沫乳花浮午盏. 蓼茸蒿笋试春盘, 人间有味是清欢.',
                 fregtime=datetime.now()),
            Food(fid=17, tid=25, fname='冰沙餐饮',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc22baeccf5.jpg', fprice=8, forder=1,
                 fdesc='天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。 形美味浓鲜果珍，健脾润肺九州闻。 产销两旺年超亿，绿色“香田”出国门。',
                 fregtime=datetime.now()),
            Food(fid=18, tid=40, fname='五彩水果汁',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc27a7f3f6b.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=19, tid=25, fname='火山冰沙',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc233ad861d.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=20, tid=41, fname='蓝莓酱沙冰',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc23ba2900e.jpg', fprice=0, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=21, tid=15, fname='粉蒸牛肉',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3b2132278.jpg', fprice=40, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=22, tid=25, fname='水果魔方',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc24512e9c1.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=23, tid=25, fname='巧克力樱桃甜点',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc24878e2f1.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=24, tid=25, fname='树莓香草雪糕',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc24bfd5442.jpg', fprice=8, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=25, tid=25, fname='水果沙拉',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc24e7d52e6.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=26, tid=42, fname='西瓜芒果奶昔',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc2513180f3.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=27, tid=25, fname='水晶草莓',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc2553d94d3.jpg', fprice=8, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=28, tid=37, fname='拉花咖啡',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc27e146137.jpg', fprice=10, forder=1,
                 fdesc='濒危物种叹珍稀，繁育放流举世奇。 翘企明年鱼上市，佳肴佐酒欲涎垂。 天然食品神，返扑又归真。绿色无污染，清醇可健身。 田畴千里碧，棚室四时春。淡饭粗茶饱，青蔬弥足珍。',
                 fregtime=datetime.now()),
            Food(fid=29, tid=15, fname='椒香口水手撕鸡',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3b7fe2e8c.jpg', fprice=35, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=30, tid=15, fname='歌乐山辣子鸡',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3bad1708a.jpg', fprice=35, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=31, tid=15, fname='宫保鸡丁',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3bd4d7b9c.jpg', fprice=36, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=32, tid=15, fname='崂山蘑菇毽子肉',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3c2872a3a.jpg', fprice=40, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=33, tid=15, fname='老成都鸡米芽菜',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3c674077e.jpg', fprice=40, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=34, tid=15, fname='蚂蚁上树',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3c8e9cb23.jpg', fprice=39, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=35, tid=15, fname='松仁扒脆皖鱼',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3ce075f0c.jpg', fprice=40, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=36, tid=15, fname='万喜八宝烟熏肠',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3d2cd68ec.jpg', fprice=35, forder=1,
                 fdesc='此州乃竹乡，春笋满山谷。 山夫折盈抱，抱来早市鬻。 物以多为贱，双钱易一束。 置之炊甑中，与饭同时熟。 紫箨坼故锦，素肌掰新玉。 每日遂加餐，经时不思肉。 久为京洛客，此味常不足。 且食勿踟蹰，南风吹作竹。',
                 fregtime=datetime.now()),
            Food(fid=37, tid=31, fname='中药鸡汤',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3db2cfc13.jpg', fprice=39, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。 暂借垂莲十分盏，一浇空腹五车书。 青浮卵碗槐芽饼，红点冰盘藿叶鱼。 细雨斜风作小寒，  淡烟疏柳媚晴滩.  入淮清洛渐漫漫，  雪沫乳花浮午盏. 蓼茸蒿笋试春盘, 人间有味是清欢.',
                 fregtime=datetime.now()),
            Food(fid=38, tid=44, fname='韩国火锅',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3f1620ef9.jpg', fprice=45, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=39, tid=45, fname='特质砂锅',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3f77e6e20.jpg', fprice=45, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=40, tid=46, fname='经典火锅',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc3fac1853e.jpg', fprice=45, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=41, tid=26, fname='大虾牛腩饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc40de9d72f.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=42, tid=26, fname='海参牛腩饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc410a53153.jpg', fprice=25, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=43, tid=26, fname='金针菇肥牛盖饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc4130ce1c5.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=44, tid=48, fname='美味盖鱼饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc415b1ffbb.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=45, tid=19, fname='金光四溢',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc8eaf149fc.jpg', fprice=30, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=46, tid=22, fname='红烧茄子',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc8ee8618c3.jpg', fprice=35, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=47, tid=23, fname='红烧鸡腿',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc8f110d265.jpg', fprice=50, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=48, tid=21, fname='青春如虹',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc8f76d4a6e.jpg', fprice=25, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=49, tid=59, fname='烧麦',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc8fa12a233.jpg',
                 fprice=15, forder=1, fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=50, tid=27, fname='草莓小虾',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc8fdcd8fc1.jpg', fprice=35, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=51, tid=27, fname='千层豆腐',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc901433aa4.jpg', fprice=30, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=52, tid=49, fname='韩国泡饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc95f53ac02.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=53, tid=50, fname='喜沙肉盖饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc964ad89de.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=54, tid=55, fname='黄金盖饭',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc9682bb47d.jpg', fprice=18, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=55, tid=57, fname='豆饼面条',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc96c751a2d.jpg', fprice=15, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=56, tid=57, fname='清淡面条',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc96fad99fc.jpg', fprice=13, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=57, tid=58, fname='海绵宝宝',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc972152868.jpg', fprice=5, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=58, tid=59, fname='寿司拼盘',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc975e311c0.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=59, tid=28, fname='碳烤生蚝',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc978d44a54.jpg', fprice=20, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=60, tid=60, fname='鲜虾米线',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc97c9e34b7.jpg', fprice=15, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now()),
            Food(fid=61, tid=19, fname='秘制翅扇贝',
                 fpic='https://web-final.oss-cn-beijing.aliyuncs.com/foods/52fc98252b588.jpg', fprice=30, forder=1,
                 fdesc='枇杷已熟粲金珠，桑落初尝滟玉蛆。', fregtime=datetime.now())
        ]
        for food in foods:
            db.session.add(food)
        db.session.commit()

# 定义 FType 模型
class FType(db.Model):
    __tablename__ = 'ftype'
    tid = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(255), nullable=False)
    @staticmethod
    def init_db():
        ftypes = [
            FType(tid=14, tname='冰饮'),
            FType(tid=15, tname='川菜'),
            FType(tid=19, tname='湘菜'),
            FType(tid=21, tname='浙菜'),
            FType(tid=22, tname='京菜'),
            FType(tid=23, tname='东北风味'),
            FType(tid=25, tname='甜品'),
            FType(tid=26, tname='中式盖饭'),
            FType(tid=27, tname='家常菜'),
            FType(tid=28, tname='日本锄烧火锅'),
            FType(tid=29, tname='四川火锅'),
            FType(tid=30, tname='重庆火锅'),
            FType(tid=31, tname='养生'),
            FType(tid=32, tname='滋补'),
            FType(tid=33, tname='米粉'),
            FType(tid=37, tname='咖啡'),
            FType(tid=38, tname='冰淇淋'),
            FType(tid=39, tname='啤酒'),
            FType(tid=40, tname='果汁'),
            FType(tid=41, tname='冰沙'),
            FType(tid=42, tname='奶昔'),
            FType(tid=43, tname='汽水'),
            FType(tid=44, tname='韩国火锅'),
            FType(tid=45, tname='特质砂锅'),
            FType(tid=46, tname='经典火锅'),
            FType(tid=47, tname='创新火锅'),
            FType(tid=48, tname='日式盖饭'),
            FType(tid=49, tname='韩国泡饭'),
            FType(tid=50, tname='家常盖饭'),
            FType(tid=52, tname='安神'),
            FType(tid=53, tname='保健'),
            FType(tid=55, tname='经典盖饭'),
            FType(tid=56, tname='聚气'),
            FType(tid=57, tname='面条'),
            FType(tid=58, tname='蛋糕'),
            FType(tid=59, tname='馒头'),
            FType(tid=60, tname='过桥米线')

        ]
        for ftype in ftypes:
            db.session.add(ftype)
        db.session.commit()

# 定义 User 模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    @staticmethod
    def init_db():
        users = [
            User(id=25, account='admin', password='admin123'),
            User(id=26, account='weTcQHQwi1', password='4viT7DaZLM'),
            User(id=27, account='i0inhHj7cF', password='ZBNz5xrJ6a'),
            User(id=28, account='2OFYILyUox', password='3SlGVzI7WH'),
            User(id=29, account='OPkQFCecKE', password='pRSwP3c1CR'),
            User(id=30, account='iZeZj7WBHB', password='WNHYhVJnnw'),
            User(id=31, account='j5Xu4J6Kra', password='BNj6fPh3Cb'),
            User(id=32, account='0OSliGBU8G', password='TPFP7eeECS'),
            User(id=33, account='TsRQ1tluXC', password='WXd6fjqKqx'),
            User(id=34, account='DqzxWRU5jA', password='izsytaQED7'),
            User(id=35, account='oxgL2ai7oz', password='HjnnUADcdI'),
            User(id=36, account='BVKkCDC9Wk', password='nD7ghKXKAa'),
            User(id=37, account='ZVzqgdl4r8', password='QvtIwTF3fU'),
            User(id=38, account='a02XEpkYkJ', password='cJ1HERAapm'),
            User(id=39, account='rtSnmTCY30', password='EMPWJqkfPf'),
            User(id=40, account='aeCxJbFFrz', password='nnijG0Agsx'),
            User(id=41, account='tc1EtH8S5z', password='8sUfFiAB8m'),
            User(id=42, account='3FdcQM6nAR', password='UhqlOupCwd'),
            User(id=43, account='2HLcGciEPB', password='kmqIlyeARX'),
            User(id=44, account='zhlbta8tqs', password='5jOfJt6LPq'),
            User(id=45, account='MKr0LJRGT6', password='GCJAWh3Hz1'),
            User(id=46, account='oel1vR1t3I', password='1iZpzUJSN2'),
            User(id=47, account='sdfYSPKkcV', password='b0y6T8zpiv'),
            User(id=48, account='Ecg6C657nb', password='LxDZ321bFu'),
            User(id=49, account='YFZxqv8c1f', password='fnIz85Vdji'),
            User(id=50, account='DqALKaRuNH', password='GBMZbZVpSE')

        ]
        for user in users:
            db.session.add(user)

        # 提交数据库会话
        db.session.commit()