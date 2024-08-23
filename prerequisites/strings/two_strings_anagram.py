def checkAnagrams1(string1,string2):
    x = sorted(string1)
    y = sorted(string2)
    
    if x == y:
        print("Strings Are Anagram")
        return True
    else:
        print("Strings Are Not Anagram")
        return False
    
def check_Anagrams2(string1,string2):
    x = sorted(string1)
    y = sorted(string2)
    # Case:1 Check the length of both the strings
    if len(string1)!= len(string2):
        print("Strings Are Not Anagram")
        return False
    # Case:2 Check if every character of str1 and str2 matches with each other
    else:
        for char in range(len(string1)):
            if x[char]!= y[char]:
                print("Strings Are Not Anagram")
                return False
            
        print("Strings Are Anagram")    
        return True

def check_Anagrams3(string1,string2):
    # Convert both strings to uppercase to handle both cases consistently
    string1 = string1.upper()
    string2 = string2.upper()
    
    if(len(string1) != len(string2)):
        print("The given strings are not Anagrams! As the length of both the strings are different.")
        return False
    else:
        # Create a count array of size 26 for characters A-Z
        count = [0] * 26
        
        # Count frequency of each character in string1
        for char in string1:
            count[ord(char) - ord('A')] += 1
        
        # Subtract frequency of each character in string2
        for char in string2:
            count[ord(char) - ord('A')] -= 1
        # Check if any frequency is non-zero
        for freq in count:
            if freq != 0:
                print("The given strings are not Anagrams! As the count of characters is different.")
                return False
            
        print("The given strings are Anagrams!")
        return True

            
if __name__ == "__main__":
    string1 = "ARIEF"
    string2 = "IREFA"
    
    checkAnagrams1(string1,string2)
    check_Anagrams2(string1,string2)
    check_Anagrams3(string1,string2)