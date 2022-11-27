count: int = 0
iterations: int = 0


def createSample(): print('create sample')


def factorize(): print('factorize')


# Compare the product calculated factors witht the original product
def checkValidity(): print('check') 
  

def main(iterations):
    
    for count in range(iterations):
        createSample()
        factorize()
        checkValidity()
        
    

if __name__ == '__main__':
    
    #iterations = int(input('Set number of iterations: '))
    iterations = 1
    
    main(iterations)