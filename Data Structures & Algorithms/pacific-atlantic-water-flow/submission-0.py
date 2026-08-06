class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts):
            vis = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if (nr, nc) not in vis and heights[nr][nc] >= heights[r][c]:
                            vis.add((nr, nc))
                            q.append((nr, nc))
            return vis

        pac_starts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atl_starts = [(ROWS - 1, c) for c in range(COLS)] + [
            (r, COLS - 1) for r in range(ROWS)
        ]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        return [[r, c] for (r, c) in pac & atl]