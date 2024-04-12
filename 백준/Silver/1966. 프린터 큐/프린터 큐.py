# 중요도의 최댓값을 구한 후 큐에서 해당 최댓값의 중요도를 가진 문서가 나올때까지 문서를 뒤로 보낸다.
from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    documents = deque(map(int, input().split()))
    idxList = deque(range(N))
    cnt = 1
    while True:
        _max = max(documents)
        if documents[0] == _max:
            if idxList[0] == M:
                print(cnt)
                break
            else:
                documents.popleft()
                idxList.popleft()
                cnt += 1
        else:
            documents.append(documents.popleft())
            idxList.append(idxList.popleft())
