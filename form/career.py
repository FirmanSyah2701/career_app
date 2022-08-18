from fastapi import Request
from typing import List, Optional
import re

class CareerForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.student_parent_number: Optional[str] = None
        self.student_name: Optional[str] = None
        self.student_class: Optional[str] = None
        self.gender: Optional[str] = None
        self.school_id: Optional[str] = None
        self.major: Optional[str] = None
        self.cp_one: Optional[str] = None
        self.cp_two: Optional[str] = None
        self.ce_one: Optional[str] = None
        self.ce_two: Optional[str] = None
        self.mcd_one: Optional[str] = None
        self.mcd_two: Optional[str] = None
        self.mcd_three: Optional[str] = None
        self.wwi_one: Optional[str] = None
        self.wwi_two: Optional[str] = None
        self.wwi_three: Optional[str] = None
        self.wwi_four: Optional[str] = None
        self.wwi_five: Optional[str] = None
        self.pgw_one: Optional[str] = None
        self.pgw_two: Optional[str] = None
        self.pgw_three: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.student_parent_number = form.get("student_parent_number")
        self.student_name = form.get("student_name")
        self.student_class = form.get("student_class")
        self.gender = form.get("gender")
        self.school_id = form.get("school_id")
        self.major = form.get("major")
        self.cp_one = form.get("cp_one")
        self.cp_two = form.get("cp_two")
        self.ce_one = form.get("ce_one")
        self.ce_two = form.get("ce_two")
        self.mcd_one = form.get("mcd_one")
        self.mcd_two = form.get("mcd_two")
        self.mcd_three = form.get("mcd_three")
        self.wwi_one = form.get("wwi_one")
        self.wwi_two = form.get("wwi_two")
        self.wwi_three = form.get("wwi_three")
        self.wwi_four = form.get("wwi_four")
        self.wwi_five = form.get("wwi_five")
        self.pgw_one = form.get("pgw_one")
        self.pgw_two = form.get("pgw_two")
        self.pgw_three = form.get("pgw_three")

    async def is_valid(self):
        if not self.student_parent_number:
            self.errors.append("NIS harus diisi!")
        if not re.match("^\\d+$", self.student_parent_number):
            self.errors.append("NIS hanya boleh diisi angka!")
        if not self.student_name:
            self.errors.append("Nama harus diisi!")
        if not re.match("[a-zA-Z\s\'\.]*$", self.student_name):
            self.errors.append("Nama tidak valid!")
        if not self.student_class:
            self.errors.append("Kelas harus diisi!")
        if not self.gender:
            self.errors.append("Jenis Kelamin harus diisi!")
        if not self.school_id:
            self.errors.append("Asal sekolah harus diisi!")
        if not self.major:
            self.errors.append("Jurusan harus diisi!")
        if not self.cp_one or not self.cp_two or not self.ce_one or not self.ce_two or not self.mcd_one or not self.mcd_two or not self.mcd_three or not self.wwi_one or not self.wwi_two or not self.wwi_three or not self.wwi_four or not self.wwi_five or not self.pgw_one or not self.pgw_two or not self.pgw_three:
            self.errors.append("Kuesioner harus diisi!")
        if not self.errors:
            return True
        return False