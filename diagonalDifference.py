def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    
    
    n=len(arr)
    for i in range(n):
        sum1=arr[i][i]+sum1
        sum2=arr[i][n-1-i]+sum2
    return abs(sum1-sum2)
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
