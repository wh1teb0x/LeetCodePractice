# 83. Remove Duplicates from Sorted List

current pointerを用意する。
current pointerのNodeの値と、current pointerのnext pointerのNodeの値が同じ場合、current pointerのnext pointerのNodeをSkipする処理を入れる。
値が同じでない場合は、current pointerをnext pointerに移動させる。

Time Complexity: O(N)
Space Complexity: O(1)


- I initialize the current pointer to the head of the linked list.
- While the current node and the next node exist, I compare their values.
- If the values are equal, I skip the next node by updating current.next.
- Otherwise, I move the current pointer to the next node.