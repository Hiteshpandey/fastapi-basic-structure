from pydantic import basemodel

class mx(basemodel):
    domain: str
    email: str
