import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dict(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) >0:
        print("did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        
        answer = input("press Y for yes or N for no: ")
        if answer.upper() == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            print("did you mean %s instead?" %get_close_matches(word,data.keys())[1])
            ans = input("enter Y if yes or N if no: ")
            if ans.upper() == "Y":
                return data[get_close_matches(word,data.keys())[1]]
            else:
                return "no such words exists"
            
                

    else :
        return "no such words exists"

     
print("\nhello! welcome to the English Dictionary")
while True:
    
    param = input("Enter the word whose meaning you want to know:\n")
    if param !="\end":
        output = dict(param)
        if type(output) is list:
            print("the meaning is:")
            for item in output:
                print(item)
        else:
            print(output)
        A=input("\n\n Do you want to know the meaning of another word?,\n press Y for yes or N for no: ")
        if A.lower() == "y":
            continue
        else:
            print("\nokay thank you for choosing us, hope to see you soon!\n")
            break
      
             
    else:
        break
                    
                    
                    
                
      








