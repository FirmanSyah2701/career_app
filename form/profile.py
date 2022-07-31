from fastapi import Request
from typing import List, Optional


class ProfileForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.email: Optional[str] = None
        self.school_name: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.email = form.get("email")
        #self.school_name = form.get("school_name")
    
    async def is_valid(self):
        if not self.email:
            self.errors.append("Email is required")
        if not self.email.__contains__("@"):
            self.errors.append("Email is invalid")
        if not self.errors:
            return True
        return False

    async def is_valid_admin(self):
        if not self.email:
            self.errors.append("Email is required")
        if not self.email.__contains__("@"):
            self.errors.append("Email is invalid")
        if not self.school_name:
            self.errors.append("School name is required")
        if not self.errors:
            return True
        return False