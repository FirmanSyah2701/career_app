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
        if not self.email or not self.password: 
            self.errors.append("Email dan password tidak boleh kosong")
        if not self.errors:
            return True
        return False