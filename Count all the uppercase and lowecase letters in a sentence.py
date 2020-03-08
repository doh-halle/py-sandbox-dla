def upper_lower(strng):
    dtnry={"upper":0, "lower":0}
    for chtr in strng:
        if chtr.isupper():
            dtnry["upper"]+=1
        elif chtr.islower():
            dtnry["lower"]+=1
        else:
            pass
    print("Original String : ", strng)
    print("No. of Upper case Characters : ", dtnry["upper"])
    print("No. of Lower case Characters : ", dtnry["lower"])