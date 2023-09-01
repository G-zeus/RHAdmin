employee_update_schema = {
    "name": {'type': 'string', 'required': True},
    "last_name": {'type': 'string', 'required': True},
    "second_name": {'type': 'string', 'required': True},
    "emergency_contact": {'type': 'string', 'required': True},
    "emergency_phone": {'type': 'string', 'required': True},
    "is_active": {'type': 'boolean', 'required': True},
    "blood_type": {'type': 'string', 'required': False,},
    "position": {'type': 'string', 'required': False}
}



