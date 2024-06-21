from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class ItemType(Enum):
    item = 0
    bom = 1
    service = 2


class Base(BaseModel):
    created_at: datetime
    created_by: str
    last_modified_at: datetime
    last_modified_by: str

class User(Base):
    username: str
    password: str
    email: str
    phone: int
    first_name: str
    middle_name: str
    last_name: str
    full_name: str
    is_disabled: bool
    is_admin: bool

class Item(Base):
    number: int
    name: str
    cost: float
    assemble: bool
    itemtype: ItemType

class UpdateItem(Base):
    name: str|None = None
    price: float|None = None
    brand: str|None = None

class Bom(Base):
    line_number: int
    item: Item
    quantity: int

class BomVersion(Base):
    version: int
    bom: Bom

