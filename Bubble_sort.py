n = input().strip()
input_to_char = input().strip().split() #輸入字元，並將輸入字元變成一個list
char = []
swaps = 0

for i in range(int(n)):
    char.append(input_to_char[i]) #因為上面input_to_char沒有規定可以輸入幾個字元，也就是使用者可能會輸入大於n個字元，那這邊的for迴圈就是在規定char這個list只能有使用者輸入的前n個字元
    
for i in range(int(n)-1): #外層迴圈，來看要做幾輪的交換
    for j in range(int(n)-1-i): #內層迴圈，來看一輪要做幾次的交換
        if(ord(char[j]) > ord(char[j+1])): #比較ASCII碼的大小來做交換
            char[j], char[j+1] = char[j+1], char[j]
            swaps += 1

print(" ".join(char)) #將list轉換成字串
print(f"swaps={swaps}")

'''
外層迴圈 for i in range(n-1)
意思：總共需要做 n-1 輪比較
每一輪都能把最大的還沒排序的元素移到正確位置
為什麼是 n-1 而不是 n？
最後一個元素自動就排好了，不需要再比較

內層迴圈 for j in range(n-1-i)
每一輪只需要比較到「最後還沒排序的位置」
因為前面已經排序好的元素不用再比了
每次迴圈比較 chars[j] 與 chars[j+1]，若前者大就交換
'''
