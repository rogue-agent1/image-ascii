#!/usr/bin/env python3
"""image_ascii - Generate ASCII art patterns and conversions."""
import sys, math
def gradient_bar(width=60):
    chars=" .:-=+*#%@"
    return "".join(chars[int(i/width*(len(chars)-1))] for i in range(width))
def circle(radius=10):
    for y in range(-radius,radius+1):
        line=""
        for x in range(-radius*2,radius*2+1):
            if (x/2)**2+y**2<=radius**2: line+="*"
            else: line+=" "
        print(line)
def wave(width=60,height=10,freq=2):
    for y in range(height):
        line=""
        for x in range(width):
            v=math.sin(x/width*math.pi*freq*2+y/height*math.pi)
            idx=int((v+1)/2*(9))
            line+=" .:-=+*#%@"[idx]
        print(line)
def plasma(w=60,h=25):
    for y in range(h):
        line=""
        for x in range(w):
            v=(math.sin(x/5)+math.sin(y/3)+math.sin((x+y)/7)+math.sin(math.sqrt(x**2+y**2)/4))/4
            idx=int((v+1)/2*9)
            line+=" .:-=+*#%@"[idx]
        print(line)
if __name__=="__main__":
    cmd=sys.argv[1] if len(sys.argv)>1 else "plasma"
    if cmd=="gradient": print(gradient_bar())
    elif cmd=="circle": circle(int(sys.argv[2]) if len(sys.argv)>2 else 10)
    elif cmd=="wave": wave()
    elif cmd=="plasma": plasma()
    else: print("Commands: gradient, circle, wave, plasma")
