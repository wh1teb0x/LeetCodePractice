# 6. Zigzag Conversion

くだりの際、それぞれの場所が見つかってから　N + (N - 2)  ごとに現れると理解。
2行目は、登っていく際に見つかるものが、下る際に見つかってからN番後に現れる
3行目は N - 2 番後に現れる
4行目は N - 3 番後に現れる
......
.....
N行目は登るものがない。N + (N - 2) ごとに現れる

これをどう実装すればいいのかわからなかったので他の人の回答を見る。
https://github.com/kazuki-official/leetcode/pull/61/changes

## soleve_1
rowごとの文字列を用意。
下がる時と登る時で処理の対応を変える。
下がるか登るかの判断は、現在のRowの場所が、0か、numRows - 1の時。
0の場合は、次は下がる。
numRows - 1 の場合は、次は上がる。

Time complexity: O(N)
Space Complexity: O(N)

## solve_2
rowsの中で用意するものを文字列ではなく配列にしたほうが処理が早いだろうと思った。
文字列だとimmutableなので、文字をAppendした際に、文字列をコピーすることで、O(N)毎回かかるから。
配列の場合、O(1)で処理がおわる。

## solve_3 
row_charsとしていたが、rowの複数形なので、char_rowsに命名変更。

## solve_4
sole 3 の繰り返し。
