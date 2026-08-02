# 206. Reverse Linked List

previous pointer, current pointerを用意して操作する。

current pointerがNoneでない場合に、
- current pointerのnext Nodeをtmpとして保存しておく
- current pointerのnextを、previous pointerに変更する
- previous pointerをcurrent pointerに更新する
- current pointerを、tmpとして保存していた状態に更新する

最後にpreviousをreturnすると、更新したLinked Listの最初のNodeを返却することができる。

Time Complexity: O(N)
Space Compkexity: O(1)

## solve_1.py

想定したやり方で解いた

## solve_2.py

https://github.com/t0hsumi/leetcode/pull/7#discussion_r1875385145 を見て、previousを返すのは確かにわかりづらいなと。

reversed_headに変更、currentもcurrent_nodeに変更。
tmp、悪い命名すぎるので、next_nodeとかの方がわかりやすいかと思い修正。

## sole_3.py

revursiveな書き方。

https://github.com/t0hsumi/leetcode/pull/7/changes#r1876218686 Optional 使う方にする。

helperを用意。method内にfunctionを書くと可読性が下がると判断し、methodとしてhelperを用意した。
(`_reverseListHelper` と、private methodにした方がいいかもしれないが、leetcodeのこの問題でそこまでしなくても可読性問題ないかと思いそのままpublic method。)