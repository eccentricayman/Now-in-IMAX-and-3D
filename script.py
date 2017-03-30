#ty @fierydarkwraith for the script :P
import math

with open("script", "w") as fd:

    end = ""
    for i in range(0, 120):
        end += "clear\n"
        end += "torus\n0 0 0 %d %d\n"%(i, 120 - i)
        end += "apply\n"
        if i < 10:
            end += "save\n anim/00%d.png\n"%(i)
        else:
            end += "save\n anim/0%d.png\n"%(i)
    print end
    fd.write(end)
