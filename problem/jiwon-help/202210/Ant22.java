import java.util.Scanner;
import java.util.ArrayList;
 
public class Ant22{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String answer = "1";
		String tempanswer = "";
		char temped = '1';
		int cnt = 0;
		char temp;
		
		for(int i = 1; i < n; i++){// i 번째 수열 구함 -> n까지.. 
			for(int j = 0; j < answer.length(); j++){// 전 answer를 이용하여 조사 -> 반복문 끝나면 i 번째 answer가 생성 
				if(j == 0){
					temped = answer.charAt(0);
				}
				temp = answer.charAt(j);
				if(temped == temp || j == 0){ // 전 문자와 같다면 
					cnt += 1;
				}else{ //전 문자어ㅘ 다르다면 ;
					tempanswer += Character.toString(temped) + Integer.toString(cnt);
					cnt = 1;
				}
				if(j + 1 == answer.length()){ //반복 마지막이라면 
					tempanswer += Character.toString(temp) + Integer.toString(cnt);
					cnt = 0;
				}
				temped = temp;
			}
			answer = tempanswer;
			tempanswer = "";
		}
		System.out.print(answer);
	}
}