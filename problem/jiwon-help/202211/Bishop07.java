import java.util.*;

/**
* bishop 한 행에 한개, 대각선 안됨. 열 겹쳐도 됨.
*
*/
public class Bishop07 {
	static HashSet<String> sets = new HashSet<String>();
	static int n;
	static String[][] board;
	public static void main(String[] args) {
	// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
			
		n = input.nextInt();
		int fx = input.nextInt();
		int fy = input.nextInt();
		
		board = new String[n][n];
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				board[i][j] = "*";
			}
		}
		board[fy - 1][fx - 1] = "B";
		bt(1);

	}
	public static boolean lcheck(int y, int x) {
		boolean tof = true;
		for(int i = 0; i < n; i++){
			if(i == x){
				continue;
			}
			if(board[y][i].equals("B")){
				tof = false;
			}
		}
		return tof;
	}
	public static boolean xcheck(int y, int x) {
		
		boolean tof = true;
		int my = y;
		int mx = x;
		
		//왼위
		while(true){
			if(0 <= y - 1 && 0<= x - 1){
				y -= 1;
				x -= 1;
				if(board[y][x].equals("B")){
					return false;
				}
			}else{
				break;
			}
		}
		y = my;
		x = mx;
		//오른위
		while(true){
			if(0 <= y - 1 && x + 1 < n){
				y -= 1;
				x += 1;
				if(board[y][x].equals("B")){
					return false;
				}
			}else{
				break;
			}
		}
		
		y = my;
		x = mx;
		//오른 아래
		while(true){
			if(y + 1 < n && x + 1 < n){
				y += 1;
				x += 1;
				if(board[y][x].equals("B")){
					return false;
				}
			}else{
				break;
			}
		}
		
		y = my;
		x = mx;
		//왼 아래 
		while(true){
			if(y + 1 < n&& 0<= x - 1){
				y += 1;
				x -= 1;
				if(board[y][x].equals("B")){
					return false;
				}
			}else{
				break;
			}
		}
		return tof;
	}
	public static void boardprint(){
		int setsize = sets.size();
		String temp = "";
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				temp += board[i][j];	
			}
		}
		sets.add(temp);
	
		if(setsize == sets.size()){
			return;
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				System.out.print(board[i][j] + " ");
				
				
			}
			System.out.println();
		}
		System.out.println();
	}
	public static void check() {
		boolean tof = true;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if("B".equals(board[i][j])){
					if(lcheck(i, j) && xcheck(i, j)){
						
					}else{
						tof = false;
					}
				}
			}
		}
		if(tof){
			boardprint();
		}
	}
	public static void bt(int cnt){
		if(cnt == n){
			check();
			return;
		}
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(!("*".equals(board[i][j]))){
					continue;
				}
				board[i][j] = "B";
				bt(cnt + 1);
				board[i][j] = "*";
			}
		}
	}


}