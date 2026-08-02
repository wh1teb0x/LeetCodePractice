# 142. Linked List Cycle II

slow, fast pointerで解けそう。

StartからConnecter Positionまでの距離をa, connecter positionからslow pointerとfast pointerが一緒になった時の場所までの距離をb,Loopになっている距離をcとする。とすると

slow pointerは a + bを移動

fast pointerは a + b + kc を移動　（何回もループする可能性がある）

a + b + kc = 2(a + b)

kc = a + b

ここで知りたいのはaの値なので、

a= kc - b

と、ここまではやり方を知ってはいるけど、ではどう実装するのか、というのがわからない。

Floyd Cycleの解説をネットで調べる。

上記の式を変形させる。

a = (k − 1)c + (c − b)

と整理すると、`c - b` は衝突地点からサイクル開始点までの距離。

したがって、スタート地点から進むポインタと、衝突地点から進むポインタを、同時に1ずつ進めて衝突する地点が、サイクル開始点となる。


## solve 1、solve 2

上記の解説を踏まえて実装。solve 2はsolve1 の繰り返し書いたもの

## solve 3

visited を記録しておくという考え方を知ったのでこちらも書いた。