import java.util.Scanner;
import java.util.ArrayList;

public class set03{
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
		String data = sc.next();
		int n = sc.nextInt();
		
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