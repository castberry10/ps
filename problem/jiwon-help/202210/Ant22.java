import java.util.Scanner;
import java.util.ArrayList;
 
public class Ant22{
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);

		while(sc.hasNextLine()) {
			String str1 = sc.nextLine();
			if(str1.equals("")){
				break;
			}
			String[] strs = str1.split(" ");
			String answer = "";
			String temp = strs[1];
			answer += strs[1] + " ";
			ArrayList<String> arrList = new ArrayList<String>();
			arrList.add(temp);
			
			for(int i = 2; i <= Integer.parseInt(strs[0]); i++){
				if(arrList.contains(strs[i])){
					break;
				}
				if(temp.charAt(temp.length() - 1) == strs[i].charAt(0)){
					
					temp = strs[i];
					answer += temp + " ";
					arrList.add(temp);
				}else{
					break;
				}
			}
			System.out.println(answer);
			
		
		}
	
	}
	
	
}