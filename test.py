
#Comment
print("hello World1")

# print("hello World2")

# print("hello World3")

#演算
print(1+1)
print(1-1)
print(10/2)
print(10*2)

#変数
size = "l_size"
num1 = 5
num2 = 5.5

print(size)
print(type(size))

print(num1)
print(type(num1))

print(num2)
print(type(num2))

print(num1 + num2)

permit  = True #False

#条件分岐と関係演算子
# if else elif
#==, !=, <, >, >=, <=
if size == "l_size":
  print('big size!')

if size != "s_size":
  print('not small size!') 

if num1 > 3:
  print('more than 3')
elif num1 == 0:
  print('it is zero')
else:
  print('less than 3')

#関数
def test_function1():
  num = 9

  if(num < 10):
    return "the num is less than 10"
  else:
    return "the num is more than 10"

print(test_function1())


def test_function2(arg):#引数有
  num = arg

  if(num < 10):
    return "the num is less than 10"
  else:
    return "the num is more than 10"

print(test_function2(15))

#list
size_list = ["s_size","m_size","l_size"]
print(size_list[0])

#for文
for index in range(11): #index以外でもいいが作法としてindexにすすのが通例　※iやcountも使われる
  print(index)
  print(test_function2(index))

for item in size_list: #listと組み合わせる場合は変数名はitemにされることが多い
  print(item)

#with
#open()
with open("./test.txt", "r")as file: #引数１⇨ファイルのパス、引数２⇨モード(書き足したい時＝w、読み込みたい時＝r、)
  print(file.read())#name(),mode()等別の関数も入れられる




