import sys, time
sys.stdin = open('input_1916.txt')
start_time = time.time()

#====================================================
from collections import defaultdict
import heapq

def dijkstra(start_point, end_point):
    
    # 시작 지점의 dist는 0이기에 초기화
    dist[start_point] = 0

    # BFS를 돌면서 비용을 초기화하고, 비용이 더 작다면 다음 탐색 노드에 넣어야 함.
    queue = []
    heapq.heappush(queue, ((0, start_point)))

    while queue:

        # heapq는 앞의 요소를 기준으로 정렬 되기에 앞에 cost가 와야함.
        # 그래서 지금 순서 반대임을 기억.
        cur_cost, cur = heapq.heappop(queue)

        # end_point면 종료
        if cur == end_point:
            return dist[cur]

        # 탐색
        temp = 0
        for next in graph[cur]:
            
            # 만약 지금까지의 누적이 현재 누적보다 작다면 skip 함.
            temp = cur_cost + next[1]
            if dist[next[0]] <= temp:
                continue

            # 아니면 최소비용 업데이트 후 추가
            dist[next[0]] = temp

            # 탐색에 추가.
            heapq.heappush(queue, ((dist[next[0]], next[0])))

N = int(input())
M = int(input())

graph = defaultdict(list)

# 그래프 구현 [도착 지점, 비용]
for edge in range(1, M + 1):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

# 출발점과 도착점 받기
start_point, end_point = map(int, input().split())

# 각 노드 까지의 거리를 갖는 dist 배열 구현
inf = int(1e9)
dist = [1e9] * (N + 1)

# 함수 구현
ans = dijkstra(start_point, end_point)
print(ans)
#====================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
1. 단순히 시작점에서 끝 지점으로 가는 최소 비용 거리를 찾는 문제

2. 단, 그래프 탐색이기에 다익스트라를 어떻게 구현하냐
    - 행렬 식으로 구현하는가.
    - 한 줄로 구현하는가.

3. 한 줄로 해보자
    - idx는 1부터 시작임.

4. defaultdict로 구현하고, 탐색?
'''

'''
< 시간 복잡도 >
- 노드의 수는 N개

- 노드마다 갈 수 있는 간선의 수는 N - 1.

- O((N - 1) * logN)
'''

'''
< 문제 정리 >
1. N 개의 도시. 
    - 1 ~ N

2. M 개의 간선

3. A에서 V로 가는데 드는 버스 비용최소화.
'''