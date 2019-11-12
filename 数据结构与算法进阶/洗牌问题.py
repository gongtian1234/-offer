# 1、洗牌问题。用Array编写洗牌问题？如何测试？(一个好的洗牌是每一张牌出现在一个地方的概率是相同的)

# 方法1：直接用python自带的包random.shuffle() #
a = [1,2,3,4,5,6,7]
import random
def shuffle_system(cards):
	random.shuffle(cards)
	return cards

print(shuffle_system(a))

# 方法二：自己用概率写一个每张牌出现在一个位置的概率都是1/n
'''
思路：先考虑第一个位置：随机从n张牌中抽取一张放在第一个位置，在该过程中每张牌被抽中的概率是1/n；
	  再开率第二个位置：从剩下的n-1张牌抽取一张放在第二个位置，在该过程中每张牌被抽中的概率是1/(n-1)，但是第一次没被抽中，概率为
	  (n-1)/n，两个一乘为1/(n-1) * (n-1)/n = 1/n;
	  接下来考虑第三个位置1/(n-2) * (n-2)/(n-1) * (n-1)/n = 1/n;
	  一次类推，可以得出每张牌出现在一个位置的概率是1/n
'''

def shuffle_correct(cards):
	for i in range(len(cards)):
		randomi = i + random.randint(0, len(cards)-i-1)
		cards[i], cards[randomi] = cards[randomi], cards[i]
	return cards

print(shuffle_correct([1,2,3,4,5,6,7]))

# 测试随机性
def test_shuffle(f):
	'''f: 指的是函数'''
	results = [[0 for i in range(10)] for j in range(10)]  # 生成一个10个长度为10的列表，列表示每一个元素，行表示该元素在该位置上出现的次数

	for i in range(5000):
		a = [k for k in range(10)]
		a = f(a)
		for j in range(len(a)):
			results[a[j]][j] += 1 # 如a[5]=3，即a中第6个位置是3，再到results中的第三个列表，给其第六个位置的元素加1
	print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in results]))

test_shuffle(shuffle_system)
print('-'*30)
test_shuffle(shuffle_correct)