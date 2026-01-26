from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be greated than 0)")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="New quantity (must be greater than 0)")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: float = Field(..., description="Total price fot this item (price * quantity)")
    image_url: Optional[str] = Field(None, descripion="Product image URL")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: Field(..., description="Total number of items in cart")