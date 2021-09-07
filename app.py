from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_migrate import Migrate

# Создаем приложение
app = Flask(__name__)

# Иницилизируем БД

basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@127.0.0.1:5431/sellers'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Создаем модель
class Advertisement(db.Model):
    __tablename__ = 'advertisement'

    advert_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<advert_id %r>' % self.advert_id


# Добавляем модель в базу данных
db.create_all()


# Создаем routes
@app.route('/')
def home():
    return ('<h1>«Flask»</h1> <h2>Домашнее задание к лекции <h2> <h3>[GET, PATCH, DEL]: api/v1/id</h3> <h3>POST: api/v1</h3>')



@app.route('/api/v1', methods=['POST'])
def post_advert():
    body = request.json
    advert = Advertisement(title=body.get("title"),
                           description=body.get("description"),
                           author=body.get("author"))
    db.session.add(advert)
    db.session.commit()
    return {'status': 201}


@app.route('//api/v1/<int:get_id>', methods=['GET'])
def get_advert(get_id):
    advert = Advertisement.query.filter_by(advert_id=get_id).first_or_404()
    return {"id": advert.advert_id,
            "title": advert.title,
            "description": advert.description,
            "created": advert.created,
            "author": advert.author
            }, {'status': 200}


@app.route('//api/v1/<int:patch_id>', methods=['PATCH'])
def patch_advert(patch_id):
    title = request.json
    Advertisement.query.filter_by(advert_id=patch_id).update(title)
    db.session.commit()
    advert_new = Advertisement.query.filter_by(advert_id=patch_id).first_or_404()
    return {"id": advert_new.advert_id,
            "title": advert_new.title,
            "description": advert_new.description,
            "created": advert_new.created,
            "author": advert_new.author
            }, {'status': 201}


@app.route('//api/v1/<int:del_id>', methods=['DELETE'])
def delete_advert(del_id):
    advert = Advertisement.query.filter_by(advert_id=del_id).first_or_404()
    db.session.delete(advert)
    db.session.commit()
    return {'status': 200}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(host='127.0.0.1', port=5000, debug=True)
