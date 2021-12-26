from flask import Flask
from flask import request
server = Flask(__name__)

import sys
#from importlib.machinery import SourceFileLoader

# sys.path.append('/Users/joyjitchatterjee/ExampleAPI/src')
sys.path.append('/Example-API/src')
import SortNumber

# from importlib.machinery import SourceFileLoader
# mymodule = SourceFileLoader('SortNumber.py','/Users/joyjitchatterjee/ExampleAPI/src/SortNumber.py').load_module()

@server.route('/sort-numbers', methods = ['GET'])
def sort_numbers():
    givenNumSet = request.args.get('num')
    givenNumSet = givenNumSet.split(",")

    for pos in range(0, len(givenNumSet)): 
        givenNumSet[pos] = int(givenNumSet[pos])
    

    numListSorted = SortNumber.Sort_Number(givenNumSet);
    
    # traverse in the string  
    stringNumListSorted = [str(num) for num in numListSorted]
    finalFormattedString = ",".join(stringNumListSorted)
    
    # return string  
    return finalFormattedString

@server.route('/sort-numbers', methods = ['POST'])
def greet_post():
    return "YOU JUST CHANGED ME!!!"

@server.route('/sort-numbers', methods = ['PUT'])
def greet_put():
    return "You Just PUT. Congrats!"

@server.route('/sort-numbers', methods = ['PATCH'])
def greet_patch():
    return "You Just PATTED. Congrats!"

@server.route('/sort-numbers', methods = ['DELETE'])
def greet_delete():
    return "You just DELETED. Congrats!"

if __name__ == "__main__":
    server.run(host='0.0.0.0')
