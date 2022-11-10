import java.util.Scanner;
import java.util.ArrayList;
import java.util.*;

public class Knap09{
	// static int answer = 0;
	static Set<String> sets = new HashSet<String>();
	static int n;
	static int w;
	static int[][] data;
	static int max = 0;
	static void bt(int w1, int v1){
		if(v1 > max){
			max = v1;
		}
		for(int i = 0; i < n; i++){
			if(data[i][0] + w1 <= w && !(sets.contains( Integer.toString(i)))){
				sets.add(Integer.toString(i));
				bt(w1 + data[i][0], v1 + data[i][1]);
				sets.remove(Integer.toString(i));
			}
			
		}
		
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		w = sc.nextInt();
		n = sc.nextInt();
		data = new int[n][2];
        for(int i = 0; i < n; i++){
            data[i][0] = sc.nextInt();
            data[i][1] = sc.nextInt();
        }
		bt(0, 0);
		System.out.print(max);
	}
	
}