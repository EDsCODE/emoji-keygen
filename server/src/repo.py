from .models import db


def get_all(model):
    data = model.query.all()
    return data


def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    db.session.commit()


def get(model, hash_key):
    data = model.query.get(hash_key)
    return data
