
# PYTHON
- [MP11704 Python也可以這樣學](https://www.drmaster.com.tw/Bookinfo.asp?BookID=MP11704#download)
- [Python從初學到生活應用超實務](https://www.drmaster.com.tw/Bookinfo.asp?BookID=MP22205)
- [MP32120 圖解資料結構-使用Python(第二版)](https://www.drmaster.com.tw/Bookinfo.asp?BookID=MP32120#download)
- [MP22154圖說演算法-使用Python(第二版)](https://www.drmaster.com.tw/Bookinfo.asp?BookID=MP22154#download)


# Python Searching algorithm
- [循序搜尋 (Sequential Search)](https://ithelp.ithome.com.tw/articles/10206787)
```python
data = [1, 2, 3, 4, 5, 6, 7, 8]

def sequential_search(data, key):
    for i in data:
        if i == key : 
            print("find the key") 
            break 
            
sequential_search(data, 3)
```
```python
data = [1, 2, 3, 4, 5, 6, 7, 8]

def sequential_search(data, key):
    tmp = [0] * (len(data) + 1)    #設一個空陣列，長度為data長度+1
    for i in range(1, len(data)):  #將data的值給到tmp
        tmp[i] = data[i - 1]
    tmp[0] = key                   #設定key值
    i = len(data)                  #設定索引並開始比較
    while tmp[i] != tmp[0]:
        i -= 1
    return i - 1                   #回傳索引

index = sequential_search(data, 2)
if index >= 0:
    print("finde the index: " + str(index))
else:
    print("can't find the index")
```
- [二分搜尋 (Binary Search)]()
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(data, key):
    #設置選取範圍的指標
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = (low + upper) / 2  #取中間索引的值
        if data[mid] < key:    #若搜尋值比中間的值大，將中間索引+1，取右半
            low = mid + 1
        elif data[mid] > key:  #若搜尋值比中間的值小，將中間索引+1，取左半
            upper = mid - 1
        else:                    #若搜尋值等於中間的值，則回傳
            return mid
    return -1


index = binary_search(data, 5)
if index >= 0:
    print("找到數值於索引 " + str(index))
else:
    print("找不到數值")
```

- [插補搜尋 (Interpolation Search)](https://ithelp.ithome.com.tw/articles/10207069)
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def interpolation_search(data, key):
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = int((upper - low) * (key - data[low]) / (data[upper] - data[low]) + low)
        if mid < low or mid > upper:
            break
        if key < data[mid]:
            upper = mid - 1
        elif key > data[mid]:
            low = mid + 1
        else:
            return mid

    return -1


index = interpolation_search(data, 6)
if index >= 0:
    print("找到數值於索引 " + str(index))
else:
    print("找不到數值")
```
