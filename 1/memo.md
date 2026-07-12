## solve 1
- for loop 2回で答えが出せる。
- Time Complexity: O(N^2)
- Space Complexity: O(1)

## solve 2
計算量をO(N)にするための方法を考える。

dictを使えばうまくいきそうだと思った。
初めにnumsのindexとvalueを全て確認。dictのkeyとしてnumsのvalue、dictのvalueとしてnumsのindexを格納するdictを用意する。

再度numsを先頭から確認する。Targetとの差分の値がdictのkeyとして存在している & 差分計算したきのnumsのindexがdictのvalueと異なる、場合に、答えとなる組み合わせとなる。

気をつける点は、この時のhashmapは1つのkeyに対して複数のvalueを持つことがある。

```
e.g. nums = [3, 3] の時、hashmap[3] = [0, 1] 
```

この時は、二番目の要素が回答の一部となる。

ここまで考えたが、実装がうまくいかず。

回答を見る。今回は回答が一意に決まるということで、numsの値とそのindexの組み合わせを全てhashmapに保存していなくても回答を得ることができるということを理解。hashmapのvalueをlistで持たない方針で実装する

## solve 3
defaultdictを使わなくても、dictでできる.

## solve 4
型宣言