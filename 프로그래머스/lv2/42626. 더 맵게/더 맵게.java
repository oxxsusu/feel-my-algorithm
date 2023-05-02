import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        
        int answer = 0;
        PriorityQueue<Integer> mh = new PriorityQueue<>();
        for (int i: scoville) {
            mh.add(i);
        }
        
        while (true) {
            int first = mh.poll();
            if (first >= K) break;
            if (mh.size() == 0) {
                answer = -1;
                break;
            }
            
            int second = mh.poll();
            int newFood = first + second*2;
            mh.add(newFood);
            answer++;
            
        }
        
        return answer;
    }
    

}