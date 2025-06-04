## four digit function ->
def is_weak_pattern(pin: str) -> bool:
    seq = [
    '0123', '1234', '2345', '3456', '4567', '5678', '6789',
    '7890', '8901', '9012', '0124', '1245', '2356', '3467',
    '4578', '5689', '6790', '7801', '8912', '9023',
    '9876', '8765', '7654', '6543', '5432', '4321', '3210',
    '2109', '1098', '0987', '9875', '8764', '7653', '6542',
    '5431', '4320', '3219', '2108', '1097', '0986', '9874',
    '8763', '7652', '6541', '5430', '4329', '3218', '2107',
    '1096', '0985']
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return True
    if pin[0] == pin[1] and pin[2] == pin[3]:
        return True
    if pin[0] == pin[2] and pin[1] == pin[3]:
        return True
    if pin == pin[::-1]:
        return True
    if pin in seq:
        return True
    return False

def char_tokenize(inputs):
    return list(inputs)


mapp = {
        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
        'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
    }

def f(given_input, mpin):
    if not given_input:
        return False
    try:
        given_input = given_input.strip().lower().replace(',', '')
        split_it = given_input.split()
        if len(split_it) == 3:
            day = split_it[0].zfill(2)
            month = split_it[1]
            year = split_it[2]
            month = mapp.get(month[:3], '00') if not month.isdigit() else month.zfill(2)
        elif len(given_input) == 8 and given_input.isdigit():
            day, month, year = given_input[:2], given_input[2:4], given_input[4:]
        else:
            print("Invalid Date format -->")
            return False

        mpin_matching_Demographic = {day + month,month + day,day + year[-2:],year[-2:] + day,      
            month + year[-2:],year[-2:] + month  ,year   
        }
        for p in mpin_matching_Demographic:
          if mpin == p:
              return True
        return False
    except Exception:
        return False

def six_digit_weak_pattern(pin: str) -> bool:
    if len(pin) != 6 or not pin.isdigit():
        return False
    seq=[
        '012345', '123456', '234567', '345678', '456789', '567890',
        '098765', '987654', '876543', '765432', '654321', '543210',
        '135790', '246810', '112233', '223344', '334455', '445566',
        '556677', '667788', '778899', '889900', '121212', '123123',
        '321321', '111111', '222222', '333333', '444444', '555555',
        '666666', '777777', '888888', '999999', '000000', '101010',
        '121314', '010203', '202122', '030405', '040506', '050607',
        '060708', '070809', '080910', '909090', '090909', '999000',
        '000999', '654987', '321789', '111000', '000111', '147258',
        '258369', '369147', '963852', '852741', '741963', '753159',
        '951357', '159357', '357159', '789456', '456123', '741852',
        '963741', '258147', '147369', '369258', '987123', '123789',
        '132435', '314159', '271828', '101112', '110011'
    ]

    if pin in seq:
        return True
    if len(set(pin)) == 1:
        return True
    if pin[:3] == pin[3:]: 
        return True
    if pin[:2] == pin[2:4] == pin[4:]:
        return True
    if pin == pin[::-1]:  
        return True
    if pin[0:2] == pin[2:4] and pin[2:4] == pin[4:6]: 
        return True

    return False


def f_six_digit(given_input,mpin):
    if not given_input:
        return False
    try:
        given_input = given_input.strip().lower().replace(',', '')
        split_it = given_input.split()
        if len(split_it) == 3:
            day = split_it[0].zfill(2)
            month = split_it[1]
            year = split_it[2]
            month = mapp.get(month[:3], '00') if not month.isdigit() else month.zfill(2)
        elif len(given_input) == 8 and given_input.isdigit():
            day, month, year = given_input[:2], given_input[2:4], given_input[4:]
        else:
            print("Invalid Date format -->")
            return False

        mpin_matching_Demographic = {
            day + month+year[-2:],         
            month + day+year[-2:],        
            day + year,  
            year + day,  
            month + year,
            year + month 
        }
        for p in mpin_matching_Demographic:
            if p == mpin:
                return True
        return False    
    except Exception:
        return False