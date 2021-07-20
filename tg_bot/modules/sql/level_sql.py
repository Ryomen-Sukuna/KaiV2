import threading
import traceback
from tg_bot.modules.sql import BASE, SESSION
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func
from sqlalchemy.dialects import postgresql


class Levels(BASE):
    __tablename__ = "levels"

    user_id = Column(Integer, primary_key=True)
    role_name = Column(String(255))

    def __init__(self, user_id, role):
        self.user_id = user_id
        self.role_name = role

    def __repr__(self):
        return f"<level {self.user_id} with role {self.role_name}>"


Levels.__table__.create(checkfirst=True)


def is_level(user_id: int, role: str = None):
    with SESSION() as local_session:
        if role:
            return bool(local_session.query(Levels).get((user_id, role)))
        return bool(local_session.query(Levels).get(user_id))


def get_level_role(user_id: int):
    with SESSION() as local_session:
        ret = local_session.query(Levels).get({"user_id": user_id})
        if ret:
            return ret.role_name
    return None


def get_levels(role: str = None):
    with SESSION() as local_session:
        if not role:
            return local_session.query(Levels).all()
        return local_session.query(Levels).filter(Levels.role_name == role).all()


def set_level_role(user_id: int, role: str):
    with SESSION() as local_session:
        try:
            # Check if the user exists first and create them if they don't.
            ret = local_session.query(Levels).get({"user_id": user_id})
            if not ret:
                ret = Levels(user_id, role)
                local_session.add(ret)
            else:
                ret.role_name = role
            local_session.commit()
            local_session.flush()
        except Exception:
            traceback.print_exc()
            local_session.rollback()


def remove_royal(user_id: int):
    with SESSION() as local_session:
        try:
            ret = local_session.query(Levels).get({"user_id": user_id})
            if ret:
                local_session.delete(ret)
            local_session.commit()
        except Exception:
            traceback.print_exc()
            local_session.rollback()
