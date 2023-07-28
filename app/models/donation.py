from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import CustomBase


class Donation(CustomBase):

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
