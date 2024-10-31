import java.util.HashSet;
import java.util.ArrayList;
public class mat {
    public static void main(String[] args) {
        String[] words = {"bog", "moon", "rabbit", "the", "bit", "raw"};
        HashSet<String> hs = new HashSet<>();
        for(String x: words){
            hs.add(x);
        }
        char[][] grid = {
            {'r', 'a', 'w', 'b', 'i', 't'},
            {'x', 'a', 'y', 'z', 'c', 'h'},
            {'p', 'q', 'b', 'e', 'i', 'e'},
            {'t', 'r', 's', 'b', 'o', 'g'},
            {'u', 'w', 'x', 'v', 'i', 't'},
            {'n', 'm', 'r', 'w', 'o', 't'}
        };
        
        String wo = "";
        ArrayList<String> arlist = new ArrayList<>();
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid.length;j++){
                wo+=grid[i][j];
                if(hs.contains(wo)){
                    arlist.add(wo);
                }
                
            }
            wo = "";
        }
        wo = "";
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid.length;j++){
                wo+=grid[j][i];
                if(hs.contains(wo)){
                    arlist.add(wo);
                }
                
            }
            wo = "";
        }
        wo = "";
        for(int i = 0; i < grid.length; i++){
            wo+=grid[i][i];
            if(hs.contains(wo)){
                arlist.add(wo);
            }
            wo = "";
        }
        wo = "";
        for(int i = grid.length - 1; i >= 0; i--){
            for(int j = 0; j  < grid.length; j++){
                wo+=grid[i][j];
                if(hs.contains(wo)){
                    arlist.add(wo);
                }
            }
            wo = "";
        }
        System.out.println(arlist);
    }
}
