import random
import numpy

score = []



   
def question():
        try:
            x=int(input(str(a)+' + '+str(b)+' = '))
            if int(x) == a+b:
                score.append(1)
                
            else:
                score.append(0)
        except:
            print('Answer must be an integer.')
            question()
        
            
            

input('Welcome to the Addition Test. Press the return key to begin.')
for i in range(5):
     a = random.randint(0,99)
     b = random.randint(0,99)
     question()           
            
print('Your score is '+str(numpy.sum(score))+' out of '+str(len(score)))  
