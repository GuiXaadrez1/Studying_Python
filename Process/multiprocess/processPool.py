import os 
import sys 
import time
import concurrent.futures

sys.path.append(
    os.path.abspath(
        os.path.join(
            __file__,'..'
        )
    )
)   

from multiprocess import calcula_soma

if __name__ == "__main__":
    
    with concurrent.futures.ProcessPoolExecutor() as executor: 
        
        cod1 = executor.submit(calcula_soma,50000000)
        cod2 = executor.submit(calcula_soma,50000000)
        
        print(cod1.result())
        print(cod2.result())