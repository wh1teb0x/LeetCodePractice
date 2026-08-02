# 20. Valid Parentheses


stackを用意する。
(), {}, [], の組み合わせのdictを用意する。
stackに順番にpushしていく。pushする際、popして、組み合わせが一致した時はそのまま。
組み合わせが一致しない場合はpush
最終的にstackが空になってなかったらFalse、空になってたらTrue

Time Complexity: O(N)

Space Complexity: O(N)