#include <iostream>
using namespace std;
int main(){
	int n;
	cin >> n;
	string s = "";
	string s1 = "";
	
	for(int i = 0; i < n; i++){
		cin >> s;
		cin >> s1;
		
		cout << "Case " << i + 1 << ": " << s1 <<", " << s<< "\n";
	}
	
	
}