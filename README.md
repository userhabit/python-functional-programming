# python-functional-programming
python functional programming basic


# 01. Functools
##### singledispatch


```python
from functools import singledispatch

@singledispatch
def fn(x):
    print(x)

@fn.register(int)
def _(x):
    print("Integer:", x)

@fn.register(str)
def _(x):
    print("String:", x)

@fn.register(float)
def _(x):
    print("Float:", x/2)
```


```python
fn('1')
```

    String: 1



```python
fn(1)
```

    Integer: 1



# 02. Itertools


```python
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']
list_c = ['user', 'habit', 'data', 'analysis']
```

### chain()
##### 모든 원소를 다 붙여주는 체인역할


```python
list(itertools.chain(list_a, list_b, list_c))
```

### zip()
##### 같은 갯수의 배열을 짝에 맞게 묶어줌


```python
list(zip(list_a, list_b))
```

### cycle()
##### range 값에 따른 일정 사이클로 반복함


```python
list(zip(itertools.cycle(range(2)), list_c))
```

### repeat()
##### 특정값을 반복함


```python
list(itertools.repeat(list_a, 3))
```

### dropwhile()
##### 람다식의 조건에 부합하지 않는 것을 드롭함


```python
list(itertools.dropwhile(lambda x: x < 2, list_a))
```

### takewhile()
##### 람다식의 조건에 부합하는 것을  가져옴


```python
list(itertools.takewhile(lambda x: x < 3, list_a))
```

### groupby()
##### 키 값을 기준으로 그룹핑함


```python
data = [
        {'name': 'A', 'age': 34},
        {'name': 'B', 'age': 34},
        {'name': 'C', 'age': 29},
        {'name': 'D', 'age': 33}
       ]

group_data = itertools.groupby(data, key=lambda x: x['age'])
for k, v in group_data:
    print('{}: {}'.format(k, list(v)))
```

