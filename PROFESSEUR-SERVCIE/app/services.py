from app.models import Professor
from app import db


def get_all_professors():
    return Professor.query.all()


def get_professor_by_id(professor_id):
    return Professor.query.get(professor_id)


def create_professor(name, email):
    new_professor = Professor(name=name, email=email)
    db.session.add(new_professor)
    db.session.commit()
    return new_professor


def delete_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
        return True
    return False
