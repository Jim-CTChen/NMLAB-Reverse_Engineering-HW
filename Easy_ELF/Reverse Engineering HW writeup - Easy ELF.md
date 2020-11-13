###### tags: `網路與多媒體實驗`
# Reverse Engineering HW writeup - Easy ELF
## Easy ELF
1. 從main function下手

![](https://i.imgur.com/3eujLiA.png)

2. 找到關鍵的calc function(renamed)
發現這邊已經cmp input[1]是否='1'，如果不是直接fail

![](https://i.imgur.com/fHem364.png)

3. 接著loc_8048469做了以下事情：
    - xor input[0], 0x34
    - xor input[2], 0x32
    - xor input[3], 0x88
    - cmp input[4], X

4. 接著下面的assembly又執行了以下
    - cmp input[5] = 0 (empty)
    - cmp input[2], 0x7C
    - cmp input[0], 0x78
    - cmp input[3], 0xDD

![](https://i.imgur.com/1mFmaYx.png)

![](https://i.imgur.com/op6cKXj.png)

5. 最終可得
    - input[0] = 0x34 xor 0x78
    - input[1] = 1
    - input[2] = 0x32 xor 0x7C
    - input[3] = 0x88 xor 0xDD
    - input[4] = X
    - 
### **flag = L1NUX**