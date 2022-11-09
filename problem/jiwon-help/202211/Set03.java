import java.util.Scanner;
import java.util.ArrayList;

public class Set03{
	// static int answer = 0;
	static int n;
	static String[] data;
	static void bt(int index){
		
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String datas = sc.next();
		n = sc.nextInt();
		data = datas.split("");
		Collections.sort(data);
		bt(0);
	}
	
	
}