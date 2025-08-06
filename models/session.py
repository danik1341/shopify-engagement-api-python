from pydantic import BaseModel
from typing import List, Optional


class CartItem(BaseModel):
    title: str
    quantity: int


class SessionEvent(BaseModel):
    type: str
    url: Optional[str] = None
    at: int


class SessionData(BaseModel):
    current_page: str
    time_on_site: int
    cart_items: List[CartItem]
    current_cart_count: int
    events: List[SessionEvent]
    user_id: Optional[str] = None
