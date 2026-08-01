# 387. First Unique Character in a String

## 1

まずはstring s の中の、それぞれの文字の数を数え上げる。
その後、先頭から見ていき、文字の数が1となっているものが答えとなる。
もしなかったら -1 を返す。

Time Complexity: O(N)
Space Complexity: O(N)

