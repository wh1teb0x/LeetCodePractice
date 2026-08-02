# 82. Remove Duplicates from Sorted List II

値が重複するノードは削除しないといけない。
重複をSearchする処理が必要。
重複のStartとEndの場所がわかったら、重複がStartノードの一個前のノードのnext Nodeを、重複がEndノードの次のNodeに変更させることで、重複は取り除くことができる。
重複を操作するためのポインタと、その一つ前にポインタ用意しておかないといけない。


## solve 1
前のnodeをcurrent_node、先のnodeをsearch_node、として、実装しようとしたが、できなかった。

ポインタごとの不変条件、内側のループ終了時点の位置、分岐ごとのポインタ更新、が整理することができなかった。

## solve 2

解答を見て作成。
previous, current というpointerを作成して進める。
currentの次のnodeが、currentの値と同じ場合に探索スタート。
探索終了時に、currentの位置は、値が異なるnodeに移っている。
そこで、previousノードの次のNodeをcurrentにすれば、重複位置を省くことができる。