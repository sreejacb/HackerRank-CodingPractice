english = int(input())
eng_sub = set(map(int, input().split()))
french = int(input())
fre_sub = set(map(int, input().split()))

print(len(eng_sub.intersection(fre_sub)))


'''The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.


Output the total number of students who have subscriptions to both English and French newspapers'''