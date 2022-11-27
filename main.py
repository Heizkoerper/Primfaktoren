import random as r

count: int = 0
iterations: int = 0

sample: tuple

validity: bool
overallValidity: bool = True

lst: list = [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
lenght: int = len(lst)


def createSample():
    
    prim1: int = r.choice(lst)
    prim2: int = r.choice(lst)
    prod: int = prim1 * prim2
    
    return prod, prim1, prim2


def factorize(pq): print(f'ToDo: Insert method to further use {pq}'); return 7, 11


# Compare the product calculated factors witht the original product
def checkValidity(p: int, q: int, pq: int): return p * q == pq
  

def main(iterations):
    
    for count in range(iterations):
        countOut = count + 1
        
        sample = createSample()
        pq, p1, p2 = sample
        print(f'Sample being used: {pq}, with factors being {p1} and {p2} - [{countOut}/{iterations}]')
        
        values = factorize(pq)
        p, q = values
        print(f'Finished calculations with result of {p} and {q} after 10 seconds')
        
        validity = checkValidity(p, q, pq)
        print(f'Finished sample [{countOut}/{iterations}] with validity being {validity}')
        
    

if __name__ == '__main__':
    
    print('Method by Martin Gebhardt', 'Code by Jonathan Schnieders', '(c) 2022 - All rights reserved', sep='\n', end='\n\n')
    print(f'Using preset data set with {lenght} objects...')
    
    #iterations = int(input('Set number of iterations: '))
    iterations = 1
    
    main(iterations)
    
#ToDo
# - Add verbose flag that gives all the values it calculates with