from collections import deque

def bfs():
    # 방문처리(남은 나이트 이동까지 세 줌)
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

    # 초기값 설정
    queue = deque([(0, 0, K, 0)])
    visited[0][0][K] = True

    while queue:
        # 꺼내기
        curr_r, curr_c, curr_k, curr_cnt = queue.popleft()


        # 도착하면 return
        if curr_r == H - 1 and curr_c == W - 1:
            return curr_cnt


        # 일반 이동 실행
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == 0:
                if not visited[nr][nc][curr_k]:
                    visited[nr][nc][curr_k] = True
                    queue.append((nr, nc, curr_k, curr_cnt + 1))

        # 나이트 이동이 남아있다면
        if curr_k > 0:
            # 나이트 이동 실행
            for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                           (1, 2), (-1, 2), (1, -2), (-1, -2)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == 0:
                    if not visited[nr][nc][curr_k - 1]:
                        visited[nr][nc][curr_k - 1] = True
                        queue.append((nr, nc, curr_k - 1, curr_cnt + 1))

    return -1

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]

print(bfs())