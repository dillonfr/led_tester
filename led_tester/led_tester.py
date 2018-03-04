# -*- coding: utf-8 -*-
class LightTester:
    Lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)] #creates multidimensional array with size N
        
    def apply(self, cmd):
        if cmd is "turn on":
            pass;
        elif cmd is "turn off":
            pass;
        elif cmd is "switch":
            pass;
    
    def count(self):
        #count the lights that are on
        return count
            


"""Main module."""
import cmd
def main(filename, N):
    Lights = LightTester(N)
    
    instructions = parseFile(filename)
    
    for cmd in instructions:
        lights.apply(cmd)
                     
    print("# occupied: #", light.count())
    