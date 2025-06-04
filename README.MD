Hello Everyone, Welcome to the Readme of this Project.
I am Dishank Jain from AI-Branch(skit-jaipur). And I have build the Solution within 2 days of the Data Science Assignment by One Banc.

Problem Statement =>
Read about MPIN that is used to access mobile banking apps. Many a times users end up setting an MPIN that is
guessable because
1. It is a commonly used MPIN eg 1122
2. It is a combination of easily known demographics of the user. Eg: if the birthdate is 02 Jan-1998 then MPIN
could be 0201 or 9802 or 0201 etc. Demographics such as these could be used alone or in a combination
a. DOB
b. Wedding Anniversary
c. Spouse birthday


1. ABOUT THE SOLUTION->
 
 a.)BUILDING DATASET-
     I have found the 4-digit MPIN dataset from Kaggle and using that, I have buid my own dataset, categorized them in weak or Strong.
 
 b.)TRAINING-> I have trained the dataset, using Logistic, XGBoost and DecisionTree with 90% accuracy.
 
 c.)ACCURACY-> The data was Baised on strong Pins, as there were 2800 strong pind and only 600 weak pins.
 
 d.)DUMPING -> After Training the model was dumped as .Joblib
 
 e.) Main.py ->It takes 20 test cases as input of 4-digit MPINS as well as 6-digit along with some Demographics(three).
 
 f.)Validation-> After input, the Validity of Pin is Checked.
 
 g.) Helper.py -> It has three functions->1. Check if the password is commonly used 
                                          2. Demographic matching for 4-digit.
                                          3. Demographic matching for 6 -digits.

 e.) six_digit.py-> contains frequently used 6-digit pattern matching function.

 f.) If the Demographics is Given then It checks the Matching function and returns the reason 

 g.) If no demographics then simply check commonly used pattern and our Model to check the Strength.


2. How to run the Solution->
   a.) pip install -r requirements.txt
   b.) install python

   c.) the structure should be ->
    data
       |_dataset
    model
       |_DecisionTree_Model.joblib
       |_vectorizer.joblib
    notebook
       |_.ipynb files
    main.py
    helper.py
    requirements.txt         
    
    d.) run Python main.py
    ->and see the results

3. 20 Test Cases with the Output given by My Solution are ->
                                                         OUTPUT->
    1. test_cases = [
    2. ["6666", None, None, None],                      # Weak mpin
    3. ["1234", None, None, None],                      # Weak mpin
    4. ["9876", "02021990", "15032020", "08081991"],    # Demographic(spouse) + weak 
    5. ["2580", "15081995", None, None],                # Commonly used
    6. ["4567", None, "28042003", None],                # Demographic match(DOB)
    7. ["2804", None, "28042003", None],                # Demographic match(SPOUSE)
    8.  ["1101", None, None, "11 jan 2003"],             # Demographic match(ANNIVERSARY) 
    9. ["2309", "23 sep 2004", None, "23112009"],       # Demographic match (BOTH)
    10. ["123456", None, None, None],                    # commonly used
    11. ["282003", None, "28042003", None],              # Demographic match(SPOUSE)
    12. ["258012", None, None, None],                    # Common 
    13. ["4312", None, None, None],                      # COMMONLY
    14. ["1122", "11121999", None, None],                # COMMONLY
    15. ["2024", None, None, None],                      # Strong
    16. ["2004", "20042004", None, None],                # Demographic 
    17. ["1109", "09112000", None, None],                # common
    18. ["765432", None, None, None],                    # common
    19. ["240501", "24 may 2001", None, None],           # Demographic
    20. ["9911", None, None, "11 nov 1999"],             # Demographic
    21. ["082001", None, "08 2001", None],]               # demographic 


THANK YOU......
