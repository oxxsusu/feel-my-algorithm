import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        List<Integer>[] adjList = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int i = 0; i < n-1; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            adjList[a].add(b);
            adjList[b].add(a);
        }
        
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < n-1; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            adjList[a].remove(Integer.valueOf(b));
            adjList[b].remove(Integer.valueOf(a));
            int diff = Math.abs(countNodes(n, adjList, a) - countNodes(n, adjList, b));
            if (diff < minDiff) {
                minDiff = diff;
            }
            adjList[a].add(b);
            adjList[b].add(a);
        }
        return minDiff;
    }
    
    private int countNodes(int n, List<Integer>[] adjList, int start) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        queue.offer(start);
        visited[start] = true;
        int count = 0;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            count++;
            for (int next : adjList[curr]) {
                if (!visited[next]) {
                    queue.offer(next);
                    visited[next] = true;
                }
            }
        }
        return count;
    }
}