# 141. Linked List Cycle

two pointersで解けそう。
slow pointer、fast pointer、を用意。
fast pointerはslow pointerよりも+1早く進む。
fast pointerがslow pointerに追いついたら、cycleがあるということ。
fast pointerがNoneにたどり着いたらcycleがないということ。

## solve 1
fast がNoneになるまで、という条件で書いた。

## solve 2
slow と fastが一致したらloopを抜けてreturn、fastがNoneになればreturn False

Time Complexity: O(N)
Space Complexity: O(1)