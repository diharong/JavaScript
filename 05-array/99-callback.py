numbers = [1, 2, 3]


def square(num):
    return num**2


new_numbers = list(map(square, numbers))
# map 함수의 특징 : 인자로 함수를 받을 수 있다.. square => 콜백함수이다. 
# 이 numbers 를 돌면서 square 를 반복하며 적용하는거다. => 순회, 반복문 
print(new_numbers)  # [1, 4, 9]
