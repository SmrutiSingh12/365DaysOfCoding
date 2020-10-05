'''
Given two strings “a” and “b”, find whether “b” exists as a substring in “a”.
Input Format
First-line will contain an integer, T, which represents the total number of test cases. Then T test cases follow. Each case will contain two lines each containing a string. First-line will contain “a” while the second line will contain “b”.
Constraints
1 ≤ T ≤ 10 1 ≤ |b| ≤ |a| ≤ 100000 All characters in a and b will be lowercase latin characters ('a'-'z').
Output Format
For each case print YES if “b” is a substring of “a” otherwise NO.
Sample Input 0
2
abcdef
def
computer
muter
Sample Output 0
YES
NO
Explanation 0
Test Case #00: Here "def" is present at the end of "abcdef". Test Case #01: Though "muter" is a subsequence here, we need it to be a substring.
'''

tno=int(input())
for _ in range(tno):
    for _ in range(1):
        a=input()
        b=input()
    if b in a:
        print("YES")
    else:
        print("NO")
    
