# -*- coding: utf-8 -*-

"""Console script for ledtester."""
class LightTester:
    Lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)] #creates multidimensional array with size N
        
    def apply(self, cmd, x1, y1, x2, y2):
        #cast the coordinates to ints
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        #make sure they are within the range of the grid
        if x1 < 0:
            x1 = 0
        elif x1 > len(self.lights)-1:
            x1 = len(self.lights)-1
        
        if x2 < 0:
            x2 = 0
        elif x2 > len(self.lights)-1:
            x2 = len(self.lights)-1
            
        if y1 < 0:
            y1 = 0
        elif y1 > len(self.lights)-1:
            y1 = len(self.lights)-1
        
        if y2 < 0:
            y2 = 0
        elif y2 > len(self.lights)-1:
            y2 = len(self.lights)-1
        
        
        if cmd == "turn on":
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.lights[i][j] = True
        
        elif cmd == "turn off":
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.lights[i][j] = False
                    
        elif cmd == "switch":
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    else:
                        self.lights[i][j] = True
        
        return 0
    
    def count(self):
        count = 0
        for i in range(0, len(self.lights)):
            for j in range(0, len(self.lights)):
                if self.lights[i][j] == True:
                    count += 1
        return count

import sys
sys.path.append('.')
import click
from ledtester import utils
import re
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")


def main(input=None):
    """Console script for ledtester."""
    N,instructions = utils.parseFile(input)
    
    Lights = LightTester(N)

    for instruction in instructions:
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        cmd = pat.match(instruction)
        #uncomment these to see what the regex has found and grouped
        #print("matched: ", cmd is not None, cmd.groups())
        #print(cmd.group(1), cmd.group(2), cmd.group(3), cmd.group(4), cmd.group(5))
        if (cmd != None):
            Lights.apply(cmd.group(1), cmd.group(2), cmd.group(3), cmd.group(4), cmd.group(5))
        else:
            continue;
        
        
    print("# occupied:", Lights.count())
    
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
