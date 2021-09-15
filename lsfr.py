"""
This is a python script to take in a polynomial and a number and spit out a random number
"""


#Main needs to take in the number of bits, the starting bits and a list of bits that will be xor'ed
def main() : 
    seed = 0b1001 # 0b means its a binary value 1111 makes it equal to 15
    currentSeed = 0b0000
    XORbits = [0,1,3]
    currentSeed = seed
    while(1) :
        print("{:04b}".format(seed)) # :04b prints a 4bit value, this will need to be changed to be the number of bits
        newbit = (currentSeed >> XORbits[0]) & 1
        for i in XORbits :
            newbit = newbit ^ ((seed >> i) & 1)
        currentSeed = (currentSeed >> 1) | (newbit << 3)
        print("{:04b}".format(currentSeed))
        if(currentSeed == seed) :
            break



if __name__ == "__main__":
    main()
