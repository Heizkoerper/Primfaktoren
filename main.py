import random as r
import time
import math

# Statistics
avgPQ: int = 0

avgN: int = 0
avgL: int = 0
avgR: int = 0

avgDuration: float

problems: int = 0
problematicSets: list = []

spanStart: int
spanEnd: int


count: int = 0
iterations: int = 0


sample: tuple


validity: bool
overallValidity: bool = True

#lst: list = [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
#lst: list = [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499]
lst: list = [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
lenght: int = len(lst)


def createSample():
    
    prim1: int = r.choice(lst)
    prim2: int = r.choice(lst)
    prod: int = prim1 * prim2
    
    return prod, prim1, prim2


def factorize(pq):
    
    # Calculate the lenght of the period of 1/pq
    remainder: int = 1
    i: int = 0
    
    while True:
        
        i += 1
        remainder = (remainder * 10) % pq
        
        if remainder == 0: raise Exception('[Fatal] 1 divided by given number is not periodical!')
        if remainder == 1: break
        
    
    l: int = i
    
    print(f'[Debug] Periodenlänge beläuft sich auf {l}') #Debug  
    
    # Prepear values for quadratic equaiton
    r: int = ((pq+1)/2) % l 
      
    # Solve for and return calculated values
    return solve(r, l, pq)



def solve(r, l, pq):
    
    n: int = -1
    found: bool = False
    
    while not found:
        
        n += 1
        
        # Precalculate root term and ensure it is greater or equal 0
        term: int = n**2 * l**2 +2*r*n*l + r**2 - pq
        if term < 0: continue
        
        q = n*l + r + math.sqrt(term)
        
        found = q.is_integer()
    
    p = n*l + r - math.sqrt(n**2 * l**2 +2*r*n*l + r**2 - pq)
    
    print(f'[Debug] Das n beläuft sich auf {n}') #Debug
    return p, q, n, l, r
        
        

# Compare the product calculated factors witht the original product and one of the calculated factors against the original ones
def checkValidity(p: int, q: int, p1: int, p2: int, pq: int): return (p * q == pq and (q == p1 or q == p2))
  

def main(iterations):
    
    global avgPQ; global avgN; global avgL; global avgR
    global problems; global problematicSets
    global spanStart; global spanEnd
    
    startOverall = time.time()
    
    for count in range(iterations):
        
        sample = createSample()
        pq, p1, p2 = sample
        print(f'Sample being used: {pq}, with factors being {p1} and {p2} - [{count+1}/{iterations}]')
        
        startCalc = time.time()
        p, q, n, l, r = factorize(pq)
        elapsed = time.time() - startCalc
        print(f'Finished calculations with result of {p} and {q} after {elapsed} seconds')
        
        validity = checkValidity(p, q, p1, p2, pq)
        print(f'Finished sample [{count+1}/{iterations}] with validity being {validity} \n')
        
        # Detect failed interations
        if not validity:
            
            problems += 1
            problematicSets.append(f'[{count+1}/{iterations} : {pq}, with factors being {p1} and {p2}]')
            
            continue #Skip statistics if not valid
        
        # Add values to statistics
        avgPQ += pq
        avgN += n
        avgL += l
        avgR += r
        
    
    elapsedOverall = time.time() - startOverall
    
    # Finish statistics
    avgPQ = avgPQ / (iterations - problems)
    avgN = avgN / (iterations - problems)
    avgL = avgL / (iterations - problems)
    avgR = avgR / (iterations - problems)
    
    avgDuration = elapsedOverall / iterations

    spanStart = lst[0]
    spanEnd = lst[lenght-1]
    
    # Output statistics
    print(f'\n\nStatistics over {iterations} iterations:')
    
    print('------------------------------------------------')
    
    print(f'Problems over Iterations:  {problems}/{iterations}')
    print(f'Sets Problems occured in:  {problematicSets if problematicSets else None}')
    
    print('------------------------------------------------')
    
    print(f'Average value for pq:  {avgPQ}')
    print(f'Average value for n:   {avgN}')
    print(f'Average value for l:   {avgL}')
    print(f'Average value for r:   {avgR}')
        
    

if __name__ == '__main__':
    
    print('Method by Martin Gebhardt', 'Code by Jonathan Schnieders', '(c) 2022 - All rights reserved', sep='\n', end='\n\n')
    print(f'Using preset data set with {lenght} objects...')
    
    #iterations = int(input('Set number of iterations: '))
    iterations = 50
    
    main(iterations)
    
#ToDo
# - Add verbose flag that gives all the values it calculates with