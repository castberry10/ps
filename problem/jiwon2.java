import java.util.Scanner;
 
public class jiwon2 {
	
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);

		while(sc.hasNextLine()) {
			String str1 = sc.nextLine();
			String[] strs = str1.split(" ");
			String answer = "";
			String temp = strs[1];
			answer += strs[1] + " ";
			ArrayList<String> arrList = new ArrayList<String>();
			
			for(int i = 2; i <= Integer.parseInt(strs[0]); i++){
				if(arrList.contains(strs[i])){
					break;
				}
				if(temp.charAt(temp.length() - 1) == strs[i].charAt(0)){
					
					temp = strs[i];
					answer += temp + " ";
				}else{
					break;
				}
			}
			System.out.println(answer);
			
		
		}
	
	}
	
	
}