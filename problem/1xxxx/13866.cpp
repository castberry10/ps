#include <iostream>

int main(){
	int a, b, c, d;
	
	std::cin >> a >> b >> c >> d;
	
	int t = (a + d)  - (c + b);
	
	if(t >= 0){
		std::cout << t;
		return 0;
	}else{
		std::cout << t * -1;
		return 0;
	}
}