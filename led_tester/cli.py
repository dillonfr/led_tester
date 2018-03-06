# -*- coding: utf-8 -*-

"""Console script for led_tester."""
class LightTester:
    Lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)] #creates multidimensional array with size N
        print(self.lights)
        
    def apply(self, cmd):
        if cmd is "turn on":
            pass;
        elif cmd is "turn off":
            pass;
        elif cmd is "switch":
            pass;
    
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
        #Lights.apply(instruction)
        
        
    print("# occupied:", Lights.count())
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
