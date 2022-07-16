from fastapi import Request
from typing import List, Optional


class RegisterForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.email: Optional[str] = None
        self.school_name: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.email = form.get("email")
        self.school_name = form.get("school_name")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 8:
            self.errors.append("Password must be > 8 chars")
        if not self.school_name:
            self.errors.append("School name is required")
        if not self.errors:
            return True
        return False