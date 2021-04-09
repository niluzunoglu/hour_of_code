# Enter your code here. Read input from STDIN. Print output to STDOUT

# HackerRank Python Challenge - Designer Door Mat Problem
# https://www.hackerrank.com/challenges/designer-door-mat/problem

numbers=input().split()
n,m=int(numbers[0]),int(numbers[1])

length = len("welcome")
length_of_pattern = 3
length_of_lines = int((m-length_of_pattern)/2)

for i in range(0,n): #rows

    if i == n//2: #middle of row, write welcome
        print()
        for i in range(0,(m-length)//2):
            print("-",end="")
            
        print("WELCOME",end="")
        
        for j in range(0,(m-length)//2):
            print("-",end="")

    else:
        if i != 0:
            print()
        for _ in range(0,length_of_lines):
            print("-",end="")

        for _ in range(0,length_of_pattern,3):
            print(".|.",end="")

        for _ in range(0,length_of_lines):
            print("-",end="")

        if i<n//2 and length_of_pattern<m-6:
            length_of_pattern += 6
            length_of_lines = int((m-length_of_pattern)/2)

        if i>=n//2 and length_of_pattern>3:
            length_of_pattern -= 6
            length_of_lines = int((m-length_of_pattern)/2)
  
