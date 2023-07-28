from sqlalchemy import Column, String, Text

from .base import CustomBase


class CharityProject(CustomBase):

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
