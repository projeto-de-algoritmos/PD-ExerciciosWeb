from functools import cmp_to_key
 
class Job:
     
    def __init__(self, start, finish, profit):
         
        self.start = start
        self.finish = finish
        self.profit = profit
 
# ordena eventos de acordo com o tempo de termino
def jobComparator(s1, s2):
     
    return s1.finish < s2.finish
 

def latestNonConflict(arr, i):
     
    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
             
    return -1

def findMaxProfitRec(arr, n):
     
    # Base case
    if n == 1:
        return arr[n - 1].profit
 
    inclProf = arr[n - 1].profit
    i = latestNonConflict(arr, n)
     
    if i != -1:
        inclProf += findMaxProfitRec(arr, i + 1)
 
    exclProf = findMaxProfitRec(arr, n - 1)
    return max(inclProf, exclProf)
 
def findMaxProfit(arr, n):
     
    # Ordena trabalhos de acordo com o tempo de término
    arr = sorted(arr, key = cmp_to_key(jobComparator))
    return findMaxProfitRec(arr, n)
 
# Driver code
values = [ (1, 4, 1), (3, 5, 2),(0,6,3),(4,7,4),(3,8,5),
          (5,9,6),(6,10,7),(8,11,8) ]
arr = []
for i in values:
    arr.append(Job(i[0], i[1], i[2]))
     
n = len(arr)
 
print("O lucro otimo é ", findMaxProfit(arr, n))
 