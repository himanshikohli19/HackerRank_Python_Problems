'''
Naggarro Question:

Money Confusion:
In a Laundry, it happens often that people forget to take their money out of their
pockets and the money is washed with the clothes. The laundry man simply takes
those wet notes out and puts them sequentially under the sunlight to dry them.
He does not mix them up, for ex: if he gets 3 notes from one cloth, he places then 
sequentially and then places the notes received from other clothes
and so on.
Shane forgot some money in his trousers and gave his clothes to the laundry man, 
afterward, when he realized his mistake, he got back to the laundry and asked for his money.
You have to tell the number of notes he forgot in his trousers if he knows
the exaxct amount he fogot in his trouser.

INPUT SPECIFICATION:
input1: Total money Shane has
input2: Total notes the laundry man has.
input3: An array of the order in which the notes are placed.

OUTPUT SPECIFICATION:
Return the number of notes Shane has return 0 if his money is not there.

EXAMPLE 1:
input1: 15
input2: 6
input3: [1,4,20,3,10,5]

Explanation:
Note in the fifth position(10) and Note in the sixth position(5) add up to 15, which is
the amount that shane forgot.
'''

input1=int(input())
input2=int(input())
input3 = list(map(int,input().split()))
count=0
if input1 in input3:
    print('number of notes: 1')
else:
    for i in range(0,input2):
        sum1=input3[i]
        for j in range(i+1,input2):
            sum1 += input3[j]
            if sum1 == input1:
                count=(j-i)+1
                print('number of notes: ',count)        

