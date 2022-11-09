import java.util.Scanner;
import java.util.ArrayList;

public class Key03{
	static String[][] a; 
	// static String[][] answer; 
	static int[] dx= { 1, 0, 1};
	static int[] dy= { 0, 1, 1};
	static int n;
	
	static String[][] dfs(int key, int x, int y, String[][] answer, String[][] b){
		// String[][] answer = new String[n][n];
		answer[y][x] = "1";
		for(int i = 0; i < 3; i++){
			if(x + dx[i] >= 0 && x + dx[i] < n && y + dy[i] < n && 0 <= y + dy[i] ) {
				if("1".equals(answer[y + dy[i]][x + dx[i]])){ //이전에 방문했다면 안감
					continue;
				}
				if(!(a[y + dy[i]][x + dx[i]].equals("0"))){ // 길이라면 
					if(a[y + dy[i]][x + dx[i]].equals("K")){ // 키가 있다면 
						key = 1; // 줍기 
						b[0][0] = "1";
					}
					b[y + dy[i]][x + dx[i]] = "1";
					return dfs(key, x + dx[i], y + dy[i], answer, b );// 다음 진행 방향
					// b[y + dy[i]][x + dx[i]] = "0";
				}
			}
		}
		// if(!(answer[n - 1][n - 1].equals("1"))){
		// 	answer[ y][x ] = "0";
		// }
		// if(x + 1 == n && y + 1 == n){
		// 	if(key == 1){
		// 		return b;
		// 	}
		// }
		return b;
		
	
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// String data = sc.next();
		n = sc.nextInt();
		a = new String[n][n];
		String[][] answer = new String[n][n];
		String[][] b = new String[n][n];
		
		for(int i = 0; i < n; i++){
			 for(int j = 0; j < n; j++){
				 a[i][j] = sc.next();
				 b[i][j] = "0";
				 answer[i][j] = "0";
			 }
		}
		// answer[0][0] = "1";
		// System.out.println("--------");
		// System.out.println(a);
		// for(int i = 0; i < n; i++){
		// 	 for(int j = 0; j < n; j++){
		// 		 System.out.print(a[i][j] + " ");
		// 	 }
		// 	System.out.println();
		// }
		answer = dfs(0, 0, 0, answer,b );
		if(!("1".equals(answer[n-1][n-1]))){
			System.out.print("NONE");
			return;
		}
		
		
		answer[0][0] = "1";
		for(int i = 0; i < n; i++){
			 for(int j = 0; j < n; j++){
				 System.out.print(answer[i][j] + " ");
			 }
			System.out.println();
		}
		
	}
	
	
}