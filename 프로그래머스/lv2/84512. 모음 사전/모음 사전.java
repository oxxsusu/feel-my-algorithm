import java.util.*;

class Solution {
    public static String[] alphabet;
    public static ArrayList<String> dict;
    
    public int solution(String word) {
        dict = new ArrayList<>();
        alphabet = new String[] {"A", "E", "I", "O", "U"};
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=1; i<6; i++) permutation(list, i);
        Collections.sort(dict);
        
        return dict.indexOf(word)+1;
    }
    
    // 중복순열
    public void permutation(ArrayList<Integer> list, int target) {
        
        if (list.size() == target) {
            StringBuilder sb = new StringBuilder();
            for (int i : list) {
                sb.append(alphabet[i]);
            }
            dict.add(sb.toString());
            return;
        }
        
        for (int i=0; i<5; i++) {
            list.add(i);
            permutation(list, target);
            list.remove(list.size()-1);
        }
    }
}