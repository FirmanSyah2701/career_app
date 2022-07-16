from fastapi import Request
from typing import List, Optional

class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.email: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.email = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.email: 
            self.errors.append("Email tidak boleh kosong")
        if not (self.email.__contains__("@")):
            self.errors.append("Email tidak valid")
        if not self.password:
            self.errors.append("password tidak boleh kosong")
        if not self.errors:
            return True
        return False