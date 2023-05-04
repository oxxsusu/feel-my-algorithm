import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = bfs(computers);
        return answer;
    }
    
    public int bfs(int[][] computers) {
        boolean[] visited = new boolean[computers.length];
        int connection = 0;
        
        for (int i=0; i<visited.length; i++) {
            if (visited[i]) continue; // 이미 방문한 네트워크의 경우 통과

            connection++;   // 연결 증가
            visited[i] = true; // 방문 처리
            ArrayDeque<Integer> q = new ArrayDeque<>();
            q.add(i);
            
            // bfs 진행
            while (!q.isEmpty()) {
                int idx = q.poll();
                visited[idx] = true;    // 방문 처리
               // 방문하지 않았고, 제자리가 아니면 큐에 추가
                for (int j=0; j<visited.length; j++) {
                    if (j!=idx && !visited[j] && computers[idx][j]==1) q.add(j);
                }
            }
        }
        
        return connection;
    }
}