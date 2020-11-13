###### tags: `網路與多媒體實驗`
# Reverse Engineering HW writeup - Easy Crack
## Easy Crack
1. 將視窗跑出來的關鍵文字當作線索，在IDA pro中查找

![](https://i.imgur.com/4351gTE.png)

![](https://i.imgur.com/S7S8qKe.png)

2. 在上面一點的地方可以發現一些判斷式

![](https://i.imgur.com/wCBk7TH.png)

3. 將判斷式的字串拼湊起來可得"a5yR3versing"
4. 最後再判斷第一個字 = x45 = E，得到"Ea5yR3versing"

![](https://i.imgur.com/SgrM6ld.png)

