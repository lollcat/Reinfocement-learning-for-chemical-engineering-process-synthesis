import numpy as np
def columnsize(N):
    # size in feet unless stated otherwise
    # heuristics taken from Ludwig Rules of Thumb

    # NB UNIT CONVERSIONS

    # height
    space = (20 / 12 + 2) / 2  # tray spacing
    trayheight = (N - 1) * space  # height due to tray spacing
    vapallowance = 4  # ft
    liqallowance = 6  # ft
    L = trayheight + vapallowance + liqallowance

    # diameter
    # classed according to heuristic ranges in order to maintain satisfactory diameters
    interval = np.linspace(27, 170, 10)
    interval = list(interval)
    LDratio = [1 / 9, 1 / 10, 1 / 11, 1 / 12, 1 / 13, 1 / 14, 1 / 15, 1 / 16, 1 / 17]
    for i in range(6):
        maximum = interval[i + 1]
        minimum = interval[i]
        if L > minimum and L < maximum:
            Di = LDratio[i] * L
            break

    if N < 11:
        raise ValueError("Too few stages- resulting column height too low")
    else:
        #print(Di)
        #print(L)
        #print(L / Di)
        return L, Di


