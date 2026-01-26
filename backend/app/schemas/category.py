from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, discription="Category name")
    slug: str = Field(..., min_length=5, max_length=100, discription="URL-friendly category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique category identifier')

    class Config:
        form_attributes = True