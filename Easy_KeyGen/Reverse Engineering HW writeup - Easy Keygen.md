###### tags: `網路與多媒體實驗`
# Reverse Engineering HW writeup - Easy Keygen
## Easy Keygen
1. 題目要求找到會產生Serial 5B134977135E7D13的name
2. 先從關鍵字"Input Name:"下手

![](https://i.imgur.com/yYunQyE.png)

3. 找到以後發現程式存了一個array，裡面有[16, 32, 48]
4. 接著發現跑了一個週期為三的迴圈，每三個就重新跑

![](https://i.imgur.com/UKzrLti.png)

5. 分析後面的迴圈後便發現，程式會將input name每三個字母與上面的array做XOR encoding
6. 寫個python 解碼name即可 name = K3yg3nm3

![](https://i.imgur.com/abJCQP8.png)
