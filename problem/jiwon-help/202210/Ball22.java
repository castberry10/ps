import java.util.Scanner;
import java.util.ArrayList;
/*
* n개의 공이있고			 5 2 	->		8   
* 1~k개를 뺄 수 있다. 	 5 3	->		13
* 경우의 수 구하기!! 		10 5	->	   464
*/
public class Ball22{
	static int answer = 0;
	static void bt(int n, int k){
		if(n == 0){
			answer += 1;
			return;
		}else{
			for(int i = 1; i <= k; i++){
				n -= i;
				if(n < 0){
					return;
				}
				bt(n, k);
				n += i;
			}
			return;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String dataline;
		while(sc.hasNextLine()) {
			dataline = sc.nextLine();
			String[] slicedata = dataline.split(" ");
			int N = Integer.parseInt(slicedata[0]);
			int K = Integer.parseInt(slicedata[1]);
			bt(N, K);
			System.out.println(answer);
			answer = 0;
		}
	}
	
	
}