import queue

if __name__ == '__main__':
    n,k=map(int,input().split())
    Q=queue.PriorityQueue()
    for i,x in enumerate(map(int,input().split())):
        Q.put((-x,i))
        for j in Q.queue:
            print(j, end= ' ')
        if i>=k-1:
            while i-Q.queue[0][1]>k-1: Q.get()
        
        print()
