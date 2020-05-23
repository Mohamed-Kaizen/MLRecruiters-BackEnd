from pydantic import BaseModel


class CreateOffer(BaseModel):

    worker: str

    description: str
