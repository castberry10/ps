#include<iostream>

using namespace std;

int main(){
	int n = 0, m = 0;
	char map[55][55] = {0};
	
	cin >> n >> m;
	
	int count = 0;
	
	for(int i = 0; i < n; i++){
		cin >> map[i];
	}
	
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(map[i][j] == '-'){
				count++;
				
				//cout << "Count from " << i << ':' << j << '\n';
				
				int k = j;
				while(map[i][k] == '-')
					map[i][k++] = ' ';
				
				
				/*cout << "Count to " << i << ':' << --k << '\n';
				for(int i = 0; i < n; i++){
					cout << map[i] << '\n';
				}*/
				
			} else if(map[i][j] == '|') {
				count++;
				int k = i;
				
				//cout << "Count from " << i << ':' << j << '\n';
				
				while(map[k][j] == '|')
					map[k++][j] = ' ';
				
				/*cout << "Count to " << --k << ':' << j << '\n';
				for(int i = 0; i < n; i++){
					cout << map[i] << '\n';
				}*/
			}
		}
	}
	
	cout << count;
	
	return 0;
}