import java.util.Scanner;
import java.util.ArrayList;
import java.util.*;

public class Find17{
	
	static int n;
	static int[][] data;
	// static 
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		data = new int[n][n];
		Deque<Integer> queueX = new LinkedList<>();
		Deque<Integer> queueY = new LinkedList<>();
		int x, y;
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0 , 0,-1, 1};
		
		for(int i = 0; i < n; i++){
			 for(int j = 0; j < n; j++){
				 data[i][j] = sc.nextInt();
			 }
		}
		
		queueY.add(0);
		queueX.add(0);
		
		while(queueX.size() != 0){
			x = queueX.pollFirst();
			y = queueY.pollFirst();
			// x = 0;
			// y = 0;
			// System.out.println(x);
			// System.out.println(x);
			
			for(int i = 0; i < 4; i++){
				if(0 <= x + dx[i] && x + dx[i] < n && 0 <= y + dy[i] && y + dy[i] < n ){
					if(data[y + dy[i]][x + dx[i]] == 1){
						queueX.add(x + dx[i]);
						queueY.add(y + dy[i]);
						data[y + dy[i]][x + dx[i]] = data[y][x] + 1;

					}
				}
			}
		}
		// for(int i = 0; i < n; i++){
		// 	 for(int j = 0; j < n; j++){
		// 		 System.out.print(data[i][j]);
		// 		 System.out.print(' ');
				 
		// 	 }
		// 	System.out.println();
		// }
		System.out.print(data[n -1][n-1]);
			
	}
	
}