import java.util.Scanner;
 
 
public class jiwon1 {
	
	public static String[] board;
	public static String[] TM = {"T","E","E","M","O"};
	public static String[] tm = {"t", "e", "e", "m", "o"};
	
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int testcase = in.nextInt(); 
		
		
		
		for(int case1 = 0; case1 < testcase; case1++){
			int m = in.nextInt(); //세로 
			int n = in.nextInt(); //가로
			
			board = new String[m];
			for(int i = 0; i < m; i++) {
				board[i] = in.next();
			}
		// 	for(int i = 0; i < m; i++){
		// 	System.out.println(board[i]);
		// }
			String[][] matrix = new String[board.length][];
			
			int r = 0;
			for (String b : board) {
				matrix[r++] = b.split("");
			}
			
			String[][] answer = new String[matrix.length][matrix[0].length]; 

			for(int i = 0; i < matrix.length; i++){ // 2중 반복문
				for(int j = 0 ; j < matrix[0].length; j++){
					answer[i][j] = answer[i][j];
				}
			}
			// 왼쪽 왼쪽위 위 오른위 오른쪽 오른아래 아래 왼쪽아래 
			// n 
			//w e
			// s
			
			for(int i = 0; i < m; i++){ //위 아래 
				for(int j = 0; j < n; j++){ // 오른 왼쪽
					// if(matrix[i][j].equals("T")){
						int N = i - 4;
						int W = j - 4;
						int E = j + 4;
						int S = i + 4;
						int ecnt; // 단어랑 얼마나 같은지 세기 
						if(0 <= W){
							ecnt = 0;
							for(int k = 0; k <= 4; k++){
								if(matrix[i][j - k].equals(TM[k]) || matrix[i][j - k].equals(tm[k])){
									ecnt++;
								}
							}
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i][j - k] = "#";
								}
							}
						}if(0 <= W && 0 <= N){
							ecnt = 0;
							for(int k = 0; k <= 4; k++){
								if(matrix[i - k][j - k].equals(TM[k]) || matrix[i - k][j - k].equals(tm[k])){
									ecnt++;
								}
							}
							
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i - k][j - k] = "#";
								}
							}
						} if(0 <= N){
							ecnt = 0;
							for(int k = 0; k <= 4; k++){
								if(matrix[i - k][j].equals(TM[k]) || matrix[i - k][j].equals(tm[k])){
									ecnt++;
								}
							}
							
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i - k][j] = "#";
								}
							}
						} if(0 <= N && E < n){
							ecnt = 0;
							for(int k = 0; k <= 4; k++){
								if(matrix[i - k][j + k].equals(tm[k]) || matrix[i - k][j + k].equals(TM[k])){
									ecnt++;
								}
							}
							
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i - k][j + k] = "#";
								}
							}
							
						} if(E < n){
							ecnt = 0;
							
							for(int k = 0; k <= 4; k++){
								if(matrix[i][j + k].equals(tm[k]) || matrix[i][j + k].equals(TM[k])){
									ecnt++;
								}
							}
							
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i][j + k] = "#";
								}
							}
						} if(E < n && S < m){
							ecnt = 0;
							
							for(int k = 0; k <= 4; k++){
								if(matrix[i + k][j + k].equals(tm[k]) || matrix[i + k][j + k].equals(TM[k])){
									ecnt++;
								}
							}
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i + k][j + k ] = "#";
								}
							}
						} if(S < m){
							ecnt = 0;
							
							for(int k = 0; k <= 4; k++){
								if(matrix[i + k][j].equals(tm[k]) || matrix[i + k][j].equals(TM[k])){
									ecnt++;
								}
							}
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i + k][j] = "#";
								}
							}
						} if(S < m && 0<= W){
							ecnt = 0;
							for(int k = 0; k <= 4; k++){
								if(matrix[i + k][j - k].equals(tm[k]) || matrix[i + k][j - k].equals(tm[k])){
									ecnt++;
								}
							}
							
							if(ecnt >= 4){
								for(int k = 0; k <= 4; k++){
									matrix[i + k][j - k] = "#";
								}
							}
						}
					// }
				}
			}
			
			
			for(int i = 0; i < m; i++){ //위 아래 
				for(int j = 0; j < n; j++){ // 오른 왼쪽
					System.out.print(matrix[i][j]);
				}
				System.out.println();
			}
			System.out.println();
		}
		
		
		
		
		
		
		// for(int i = 0; i < N; i++) {
		// 	for(int j = 0; j < N; j++) {
		// 		System.out.print(board[i][j] + " ");
		// 	}
		// 	System.out.println();
		// }
		
		
	}
	
	
	
}