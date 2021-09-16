"""
This is a python script to takes a Length, Seed, and Gates and uses those
to implement an LFSR. Prints each step in binary and the length of the 
repeating series. 
"""

LENGTH = 10             # The number of bits in the seed
SEED = 0b10000          # The seed value
GATES = [0,2,3,5]       # The P gates for the LSFR

def main() : 
    global LENGTH, SEED, GATES
    print(("{:0"+str(LENGTH)+"b}").format(SEED))
    currentSeed = SEED
    savedStates = {SEED:1}
    count = 0
    while(1) :
        newbit = (currentSeed >> GATES[0]) & 1
        for i in GATES[1:] :
            newbit = newbit ^ ((currentSeed >> i) & 1)
        currentSeed = (currentSeed >> 1) | (newbit << (LENGTH-1))
        print(("{:0"+str(LENGTH)+"b}").format(currentSeed))
        if(currentSeed in savedStates.keys()) :
            break
        savedStates[currentSeed] = 1
        count+=1
    print("The series repeats after", count, "rounds")


if __name__ == "__main__":
    main()
