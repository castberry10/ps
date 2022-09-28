#include <iostream>

int main(){
	int n, m;
    std::cin >> n >> m;
	int a = n * m;
	// std::cout << a / 2;
	if(a % 2 == 0){
		std::cout << a / 2;
	}else{
		std::cout << (a - 1) / 2;
	}
}