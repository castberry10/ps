import java.util.Scanner;
import java.util.ArrayList;
import java.util.*;

public class Delivery17{
	// static int answer = 0;
	// static Set<String> sets = new HashSet<String>();
	static Set<String> printsets;
	static int n;
	static int w;
	static int[][] data;
	static int max = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		w = sc.nextInt();
		n = sc.nextInt();
		data = new int[n][2];
		Set<String> sets = new HashSet<String>();
        
		bt(0, 0, sets);
		System.out.println(max);
		System.out.print("{ ");
		
		// System.out.println(printsets.size() + "---------------");
		Iterator<String> iter = printsets.iterator(); 
		while(iter.hasNext()) { 
			System.out.print(Integer.toString(Integer.parseInt(iter.next())+1) + " ");
		}
		System.out.print("}");
			
	}
	
}