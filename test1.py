

if __name__ == '__main__':
    matrix=[ [input(),float(input())] for _ in range(int(input()))]
 #matrix creation [[]]
    small=float('inf')
    second_small=float('inf')
   # name_list=[]
    for name,score in matrix:
     #   if small==score:
          #  name_list.append(name)
        if small>score:
            second_small=small
            small=score
           
           # name_list=[name]
        elif second_small>score and small != score:
            second_small=score
    
    print(second_small)
   
   
