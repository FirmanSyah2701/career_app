def test_career_all_empty(client):
    data = {
        "student_parent_number": "",
        "student_name": "",
        "student_class": "",
        "gender": "",
        "school_id": "",
        "major": "",
        "cp_one": "",
        "cp_two": "",
        "ce_one": "",
        "ce_two": "",
        "mcd_one": "",
        "mcd_two": "",
        "mcd_three": "",
        "wwi_one": "",
        "wwi_two": "",
        "wwi_three": "",
        "wwi_four": "",
        "wwi_five": "",
        "pgw_one": "",
        "pgw_two": "",
        "pgw_three": ""
    }
    response = client.post('/', data=data)
    expectation_result = 'Kuesioner harus diisi!'
    print(response.context['errors'])
    assert expectation_result in response.context['errors']

def test_career_partially_empty(client):
    data = {
        "student_parent_number": "123213131",
        "student_name": "Firman Syah",
        "student_class": "XI",
        "gender": "laki-laki",
        "school_id": "1",
        "major": "TI",
        "cp_one": "",
        "cp_two": "",
        "ce_one": "",
        "ce_two": "",
        "mcd_one": "",
        "mcd_two": "",
        "mcd_three": "",
        "wwi_one": "",
        "wwi_two": "",
        "wwi_three": "",
        "wwi_four": "",
        "wwi_five": "",
        "pgw_one": "",
        "pgw_two": "",
        "pgw_three": ""
    }
    response = client.post('/', data=data)
    expectation_result = 'Kuesioner harus diisi!'
    print(response.context['errors'])
    assert expectation_result in response.context['errors']    

def test_career_student_parent_number_must_integer(client):
    data = {
        "student_parent_number": "Student Parent Number",
        "student_name": "Firman",
        "student_class": "11",
        "gender": "laki-laki",
        "school_id": "1",
        "major": "TI",
        "cp_one": "SS",
        "cp_two": "SS",
        "ce_one": "TS",
        "ce_two": "STS",
        "mcd_one": "SS",
        "mcd_two": "SS",
        "mcd_three": "S",
        "wwi_one": "S",
        "wwi_two": "SS",
        "wwi_three": "SS",
        "wwi_four": "S",
        "wwi_five": "SS",
        "pgw_one": "STS",
        "pgw_two": "SS",
        "pgw_three": "TS"
    }
    response = client.post('/', data=data)
    print(response.context['errors'])
    expectation_result = 'NIS hanya boleh diisi angka!'
    assert expectation_result in response.context['errors'] 

def test_career_invalid_student_name(client):
    data = {
        "_id": "6d40ad83-b87b-4a39-b845-f1460828d01f",
        "student_parent_number": "1805041",
        "student_name": "@1234566",
        "student_class": "11",
        "gender": "laki-laki",
        "school_id": "1",
        "major": "TI",
        "cp_one": "SS",
        "cp_two": "SS",
        "ce_one": "TS",
        "ce_two": "STS",
        "mcd_one": "SS",
        "mcd_two": "SS",
        "mcd_three": "S",
        "wwi_one": "S",
        "wwi_two": "SS",
        "wwi_three": "SS",
        "wwi_four": "S",
        "wwi_five": "SS",
        "pgw_one": "STS",
        "pgw_two": "SS",
        "pgw_three": "TS"
    }

    response = client.post('/', data=data)
    expectation_result = "Nama tidak valid!"
    print(response.context['errors'])
    assert expectation_result in response.context['errors']

def test_career_valid(client):
    data = {
        "_id": "6d40ad83-b87b-4a39-b845-f1460828d01f",
        "student_parent_number": "180504000",
        "student_name": "Firman",
        "student_class": "11",
        "gender": "laki-laki",
        "school_id": "1",
        "major": "TI",
        "cp_one": "SS",
        "cp_two": "SS",
        "ce_one": "TS",
        "ce_two": "STS",
        "mcd_one": "SS",
        "mcd_two": "SS",
        "mcd_three": "S",
        "wwi_one": "S",
        "wwi_two": "SS",
        "wwi_three": "SS",
        "wwi_four": "S",
        "wwi_five": "SS",
        "pgw_one": "STS",
        "pgw_two": "SS",
        "pgw_three": "TS"
    }

    response = client.post('/', data=data)
    expectation_result = 'Data berhasil disimpan'
    assert expectation_result in response.context['success']