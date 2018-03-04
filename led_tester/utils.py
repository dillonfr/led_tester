'''
Created on 1 Mar 2018

@author: Dillon
'''

def parseFile(input):

    if input.startswith('http'):
        # use requests
        pass
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        # haven't written the code yet...
        return N, instructions
    return

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 
                            'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 
                            'turn on 2,2 through 7,7\n']