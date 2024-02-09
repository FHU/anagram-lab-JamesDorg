#REMOVE PASS AND FIX THIS FUNCTION
def anagram(str1, str2):

    #NotSpace
    if str1.isspace() or str2.isspace():
        return False
    
    #DoctorStrings
    str1 = str1.replace(' ', '')
    str1 = str1.lower()
    str2 = str2.replace(' ', '')
    str2 = str2.lower()

    #SplitStrings
    lst1 = list(str1)
    lst2 = list(str2)

    #ChechCharacters
    for i in lst1:
        if i in lst2:
            lst2.remove(i)
        else:
            return False

    #Return
    return True


if __name__ == '__main__':

    #Two inputs

    Imp1 = input("Enter first word: ")
    Imp2 = input("Enter second word: ")

    #Print function

    print(anagram(Imp1, Imp2))