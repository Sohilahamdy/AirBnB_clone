#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a State instance."""
        super().__init__(*args, **kwargs)
