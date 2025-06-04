from helper import six_digit_weak_pattern,f_six_digit

def validate_mpin(mpin):
    if len(mpin) != 6:
        return False
    if not mpin.isdigit():
        return False
    return True
def f1(mpin, dob, spouse, wedding):
    if not validate_mpin(mpin):
        print("Not Valid Pin")
        return

    six_digit_weak_pattern1 = six_digit_weak_pattern(mpin)

    if dob is None and wedding is None and spouse is None:
        if not six_digit_weak_pattern1:
            print("MPIN is Strong")
        else:
            print("MPIN is Weak")
    else:
        flag = False
        i = 1
        if six_digit_weak_pattern1:
            print("MPIN is Weak")          
            print(f"Reason-{i} : COMMONLY_USED\n")
            flag = True
            i += 1
        if f_six_digit(dob, mpin):
            if not flag:
                print("MPIN is Weak")
            print(f"Reason-{i} : DEMOGRAPHIC_DOB_SELF\n")
            flag = True
            i += 1
        if f_six_digit(spouse, mpin):
            if not flag:
                print("MPIN is Weak")
            print(f"Reason-{i} : DEMOGRAPHIC_DOB_SPOUSE\n")
            flag = True
            i += 1
        if f_six_digit(wedding, mpin):
            if not flag:
                print("MPIN is Weak")
            print(f"Reason-{i} : DEMOGRAPHIC_ANNIVERSARY")
            flag = True
            i += 1
        if not flag:
            print("MPIN is Strong")
