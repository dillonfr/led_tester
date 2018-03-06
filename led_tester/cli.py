# -*- coding: utf-8 -*-

"""Console script for led_tester."""
class LightTester:
    Lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)] #creates multidimensional array with size N
        print(self.lights)
        
    def apply(self, cmd, x1, y1, x2, y2):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print("Params: ", cmd, x1, y1, x2, y2)
        
        if cmd == "turn on":
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.lights[i][j] = True
            print(self.lights)
        
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
        return self.lights
    
    def count(self):
        count = 0
        print("The length is: ", len(self.lights))
        for i in range(0, len(self.lights)):
            for j in range(0, len(self.lights)):
                if self.lights[i][j] == True:
                    count += 1
        return count

import sys
sys.path.append('.')
import click
import utils
import re
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")


def main(input=None):
    """Console script for led_tester."""
    print("input", input)
    
    N,instructions = utils.parseFile(input)
    
    Lights = LightTester(N)
    
    
    print("N is: ", N)
    for instruction in instructions:
        print(instruction)
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        cmd = pat.match(instruction)
        print("matched: ", cmd is not None, cmd.groups())
        print(cmd.group(1), cmd.group(2), cmd.group(3), cmd.group(4), cmd.group(5))
        Lights.apply(cmd.group(1), cmd.group(2), cmd.group(3), cmd.group(4), cmd.group(5))
        #Lights.apply(instruction)
        
        
    print("# occupied:", Lights.count())
    
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
