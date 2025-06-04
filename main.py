from helper import is_weak_pattern, char_tokenize, f
from six_digit import f1
import joblib


def validate_mpin(mpin):
    if len(mpin) != 4:
        return False
    if not mpin.isdigit():
        return False
    return True


try:
    model = joblib.load('models/DecisionTree_Model.joblib')
    vectorizer = joblib.load('models/vectorizer.joblib')
    model_available = True
except Exception as e:
    print(f"Model failed to Load, so Ignore the Model Prediction. {e}")
    model = None
    vectorizer = None
    model_available = False

def is_model_strong(mpin):
    if not model_available:
        return True
    vec = vectorizer.transform([mpin])
    prediction = model.predict(vec)
    return prediction[0] == 1

## MAIN Function->to read all the test Cases,
##  and group into strong and Weak as output->
def main(mpin, dob, spouse,wedding):
    if(len(mpin) == 6):
        f1(mpin,dob,spouse,wedding)
        return 
    if not validate_mpin(mpin):
        print("Invalid MPIN.")
        return

    if dob is None and wedding is None and spouse is None:
        pattern_check = not is_weak_pattern(mpin)

        model_check = is_model_strong(mpin)
        i = 1
        if pattern_check and model_check:
            print("MPIN is Strong.")
        else:
            print("MPIN is Weak.")
    else:
        pattern_check = not is_weak_pattern(mpin)
        model_check = is_model_strong(mpin)
        i = 1
        flag = False
        if not pattern_check and not model_check:
            print("MPIN is Weak.\n")
            print(f"Reason-{i} : COMMONLY_USED\n")
            flag = True
            i+=1
        if f(dob,mpin):
            if(flag == False):
                print("MPIN is Weak\n")
            print(f"Reason-{i} : DEMOGRAPHIC_DOB_SELF\n")
            i+=1
            flag = True
        if f(spouse,mpin):
            if(flag == False):
                print("MPIN is Weak...\n")
            print(f"Reason-{i} : DEMOGRAPHIC_DOB_SPOUSE\n")
            i+=1
            flag = True
        if f(wedding,mpin):
            if(flag == False):
                print("MPIN is Weak...\n")
            print(f"Reason-{i} : DEMOGRAPHIC_ANNIVERSARY\n")
            i+=1    
            flag = True
        if flag == False:
            print("MPIN is Strong...")            

if __name__ == "__main__":
    test_cases = [
    ["6666", None, None, None],
    ["1234", None, None, None],
    ["9876", "02021990", "15032020", "08081991"],
    ["2580", "15081995", None, None],
    ["4567", None, "28042003", None],
    ["2804", None, "28042003", None],
    ["1101", None, None, "11 jan 2003"],
    ["2309", "23 sep 2004", None, "23112009"],
    ["123456", None, None, None],
    ["282003", None, "28042003", None],
    ["258012", None, None, None],
    ["4312", None, None, None],
    ["1122", "11121999", None, None],
    ["2024", None, None, None],
    ["2004", "20042004", None, None],
    ["1109", "09112000", None, None],
    ["765432", None, None, None],
    ["240501", "24 may 2001", None, None],
    ["9911", None, None, "11 nov 1999"],
    ["082001", None, "08 2001", None],]

    for i, case in enumerate(test_cases, start=1):
        print("-----\n")
        print(f"\nTest Case- {i} => {case} \n")
        main(*case)
