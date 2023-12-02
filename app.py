import uuid
from models import Book
from flask_cors import CORS
import random
from flask import Flask, request, jsonify
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from flask import request, jsonify
from flask.views import MethodView
from models import db
from models import User
from models import Food
from models import FType

app = Flask(__name__)
CORS().init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dishes.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()
    User.init_db()
    Food.init_db()
    FType.init_db()


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome Books!'


class BookApi(MethodView):
    def get(self, book_id):
        if not book_id:
            books: [Book] = Book.query.all()
            results = [
                {
                    'id': book.id,
                    'book_name': book.book_name,
                    'book_type': book.book_type,
                    'book_prize': book.book_prize,
                    'book_number': book.book_number,
                    'book_publisher': book.book_publisher,
                    'author': book.author,
                } for book in books
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        book: Book = Book.query.get(book_id)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': book.id,
                'book_name': book.book_name,
                'book_type': book.book_type,
                'book_prize': book.book_prize,
                'book_number': book.book_number,
                'book_publisher': book.book_publisher,
                'author': book.author,
            }
        }

    def post(self):
        form = request.json
        book = Book()
        book.book_number = form.get('book_number')
        book.book_name = form.get('book_name')
        book.book_type = form.get('book_type')
        book.book_prize = form.get('book_prize')
        book.author = form.get('author')
        book.book_publisher = form.get('book_publisher')
        db.session.add(book)
        db.session.commit()
        # id, book_number, book_name, book_type, book_prize, author, book_publisher

        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据删除成功'
        }

    def put(self, book_id):
        book: Book = Book.query.get(book_id)
        book.book_type = request.json.get('book_type')
        book.book_name = request.json.get('book_name')
        book.book_prize = request.json.get('book_prize')
        book.book_number = request.json.get('book_number')
        book.book_publisher = request.json.get('book_type')
        book.author = request.json.get('book_type')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }


book_api = BookApi.as_view('book_api')
app.add_url_rule('/books', view_func=book_api, methods=['GET', ], defaults={'book_id': None})
app.add_url_rule('/books', view_func=book_api, methods=['POST', ])
app.add_url_rule('/books/<int:book_id>', view_func=book_api, methods=['GET', 'PUT', 'DELETE'])


##############################################

class GoodsApi(MethodView):
    def get(self):
        # 获取分页和过滤参数
        page = request.args.get('page', 1, type=int)
        pageSize = request.args.get('pageSize', 5, type=int)
        fname = request.args.get('fname', '')
        tname = request.args.get('tname', '')
        fprice = request.args.get('fprice', None, type=int)

        # 构建查询
        query = db.session.query(Food).join(FType, Food.tid == FType.tid)
        if fname:
            query = query.filter(Food.fname.like(f'%{fname}%'))
        if tname:
            query = query.filter(FType.tname.like(f'%{tname}%'))
        if fprice is not None:
            query = query.filter(Food.fprice <= fprice)

        # 分页查询
        paginated_goods = query.paginate(page=page, per_page=pageSize, error_out=False)
        foodList = [
            {
                "fid": food.fid,
                "fname": food.fname,
                "fregtime": food.fregtime.strftime('%Y-%m-%d'),
                "fpic": food.fpic,
                "forder": food.forder,
                "tname": food.ftype.tname,  # 可以这样访问
                "fdesc": food.fdesc,
                "fprice": food.fprice,
                "tid": food.tid
            }
            for food in paginated_goods.items
        ]

        return jsonify({
            "code": 1,
            "msg": None,
            "data": {
                "foodList": foodList,
                "total": paginated_goods.total
            },
            "map": {}
        })

    def post(self):
        # 添加食品
        data = request.json
        try:
            new_food = Food(
                fid=str(uuid.uuid4()),
                tid=data['tid'],
                fname=data['fname'],
                fpic=data['fpic'],
                fprice=data['fprice'],
                forder=data.get('forder', 0),
                fdesc=data['fdesc'],
                fregtime=datetime.now()
            )
            db.session.add(new_food)
            db.session.commit()
            return jsonify({'code': 1, 'msg': '添加成功！', 'data': None, 'map': {}})
        except Exception as e:
            return jsonify({'code': 0, 'msg': str(e), 'data': None, 'map': {}})

    def delete(self):
        # 删除食品
        data = request.json
        food = Food.query.get(data['fid'])
        if food:
            db.session.delete(food)
            db.session.commit()
            return jsonify({'code': 1, 'msg': '删除成功', 'data': None, 'map': {}})
        else:
            return jsonify({'code': 0, 'msg': '食品未找到', 'data': None, 'map': {}})

    def put(self):
        # 更新食品
        data = request.json
        food = Food.query.get(data['fid'])
        if food:
            food.tid = data.get('tid', food.tid)
            food.fname = data.get('fname', food.fname)
            food.fpic = data.get('fpic', food.fpic)
            food.fprice = data.get('fprice', food.fprice)
            food.forder = data.get('forder', food.forder)
            food.fdesc = data.get('fdesc', food.fdesc)
            db.session.commit()
            return jsonify({'code': 1, 'msg': '修改成功！', 'data': None, 'map': {}})
        else:
            return jsonify({'code': 0, 'msg': '食品未找到', 'data': None, 'map': {}})


class GoodsStatisticsApi(MethodView):
    def get(self):
        # 连接 Food 和 FType 模型，按食品类型统计每种类型的食品数量
        statistics = db.session.query(
            FType.tname.label('name'),
            func.count(Food.fid).label('value')
        ).join(Food, Food.tid == FType.tid).group_by(FType.tname).order_by(func.count(Food.fid).desc()).all()

        # 将查询结果转换为所需的格式
        data = [{'name': stat.name, 'value': stat.value} for stat in statistics]

        return jsonify({
            'code': 1,
            'msg': None,
            'data': data,
            'map': {}
        })

# 注册路由
goods_api = GoodsApi.as_view('goods_api')

app.add_url_rule('/goods', view_func=goods_api, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/goods/statistic', view_func=GoodsStatisticsApi.as_view('goods_statistic'), methods=['GET'])

######################################################


class FTypeApi(MethodView):
    def get(self, type_id):
        if type_id is None:
            # 分页参数

            page = request.args.get('page', 1, type=int)
            pageSize = request.args.get('pageSize', 10, type=int)
            tname = request.args.get('tname', '')

            query = FType.query
            if tname:
                query = query.filter(FType.tname.like(f'%{tname}%'))

            # 分页查询
            paginated_ftypes = query.paginate(page=page, per_page=pageSize, error_out=False)
            ftypes = paginated_ftypes.items
            results = [{'tid': ftype.tid, 'tname': ftype.tname} for ftype in ftypes]

            return jsonify({
                'code': 1,
                'msg': None,
                'data': {
                    'records': results,
                    'total': paginated_ftypes.total,
                    'size': pageSize,
                    'current': page,
                    'pages': paginated_ftypes.pages
                },
                'map': {}
            })

        # 获取单个类型数据
        ftype = FType.query.get(type_id)
        if ftype is None:
            return jsonify({'code': 0, 'msg': '类型未找到', 'data': {}, 'map': {}})

        return jsonify({
            'code': 1,
            'msg': None,
            'data': {'tid': ftype.tid, 'tname': ftype.tname},
            'map': {}
        })

    def post(self):
        data = request.json
        try:
            new_ftype = FType(
                tid=str(uuid.uuid4()),
                tname=data['tname']
            )
            db.session.add(new_ftype)
            db.session.commit()
            return jsonify({'code': 1, 'msg': '添加成功', 'data': None, 'map': {}})
        except Exception as e:
            return jsonify({'code': 0, 'msg': str(e), 'data': None, 'map': {}})

    def delete(self, type_id):
        # 删除类别信息
        data = request.json
        # 更新类别信息
        ftype = FType.query.get(data['tid'])
        if ftype:
            db.session.delete(ftype)
            db.session.commit()
            return jsonify({'code': 1, 'msg': '删除成功', 'data': None, 'map': {}})
        else:
            return jsonify({'code': 0, 'msg': '类型未找到', 'data': None, 'map': {}})

    def put(self, type_id):
        data = request.json
        # 更新类别信息
        ftype = FType.query.get(data['tid'])

        if ftype:
            data = request.json
            ftype.tname = data.get('tname', ftype.tname)
            db.session.commit()
            return jsonify({'code': 1, 'msg': '修改成功', 'data': None, 'map': {}})
        else:
            return jsonify({'code': 0, 'msg': '修改失败', 'data': None, 'map': {}})


# 注册路由
ftype_api = FTypeApi.as_view('ftype_api')
app.add_url_rule('/type', view_func=ftype_api, methods=['GET', 'POST', 'PUT', 'DELETE'], defaults={'type_id': None})
app.add_url_rule('/type/<int:type_id>', view_func=ftype_api, methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/type/all', view_func=ftype_api, methods=['GET'], defaults={'type_id': None})

#####################################################

class UserApi(MethodView):
    def post(self):
        # 用户登录
        data = request.json
        user = User.query.filter_by(account=data.get('account')).first()
        if user and user.password == data.get('password'):
            # 假设登录成功后返回用户信息，实际应用中可能会返回 token 等
            return jsonify({'status': 'success', 'message': '登录成功', 'user': {'id': user.id, 'account': user.account}})
        else:
            return jsonify({'status': 'error', 'message': '账号或密码错误'})

    def get(self):
        # 获取验证码
        # 生成一个简单的数字验证码，实际应用中可能会更复杂
        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return jsonify({'status': 'success', 'message': '验证码获取成功', 'code': code})

# 注册路由
user_api = UserApi.as_view('user_api')
app.add_url_rule('/user/login', view_func=user_api, methods=['POST'])
app.add_url_rule('/user/code', view_func=user_api, methods=['GET'])