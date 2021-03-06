'''
Created on 1 Mar 2018

@author: Dillon
'''
import requests

def parseFile(input):
    #read in http file
    if input.startswith('http'): 
        N, instructions = None, []
        r = requests.get(input).text
        commands = r.splitlines()
        
        N = int(commands[0])
        
        for i in range(1, len(commands)):
            instructions.append(commands[i])
        return N, instructions
    #read in local file
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = parseFile(ifile) #utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 
                            'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 
                            'turn on 2,2 through 7,7\n']