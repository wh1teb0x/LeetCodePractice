## 1

それぞれのListの先頭から計算していく。桁上げを考慮してcarryを用意し、carryも含めて計算する。

l1とl2の長さが異なる場合を考慮を途中見落として修正。

LeetcodeではOptional使う書き方になっているが、Python3.10からOptional使わない書き方ができるようになっているので、そちらに合わせる。

Space Complexit: O(1)
Time Complexity: O(max(N, M)) (N, Mは、l1とl2のListNodeのそれぞれの長さ)

## 2

- 変数名称をもっと可読性高くする名称に変更。


## Memo
- Noneではない時の判定で `is not None` を使うのか`if not` がいいのか、規約を確認。
  - https://pep8-ja.readthedocs.io/ja/latest/#section-36