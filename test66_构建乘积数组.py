'''
题目：给定一个数组A[0,1,...,n-1]，请构建一个数组B[0,1,...,n-1]，其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法

思路：
①最暴力的方法，每个B[i]都从头计算，时间复杂度为O(n)
②B[i]的计算拆分为两部分，记C[i]=A[0]*A[1]*...*A[i-1]，D[i]=A[i+1]*...*A[n-1]，其中C[i]可以自上而下的计算，D[i]可以自下而上的计算，
而C[i]=C[i-1]*A[i-1], D[i]=D[i+1]*A[i+1], 时间复杂度为O(n)
'''
def multipy(numbers):
    if numbers is None or len(numbers)<=1:
        return []
    bi = []
    ci = []
    di = []
    nLen = len(numbers)
    for i in range(nLen):
        if i==0:
            ci.append(1)
        else:
            ci.append(ci[-1]*numbers[i-1])
        if (nLen-1)-i==(nLen-1):
            di.append(1)
        else:
            di.append(di[-1]*numbers[-i])
    di = di[::-1]
    for i in range(nLen):
        bi.append(ci[i]*di[i])
    return bi

if __name__ == '__main__':
    print(multipy([1,2,3,4]))
    print(multipy([-1,2,-3,4]))
