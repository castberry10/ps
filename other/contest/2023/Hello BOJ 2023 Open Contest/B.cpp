#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#define endl '\n'
using namespace std;
vector<int> a;

int n, k;
int answer = -1;
int tempanswer = 0;
int temp = -1;

int main(void){
    vector<int> a;
	cin >> n >> k;
    a.assign(n, 0);
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
    vector<vector<int>> templist;
	vector<int> tt(2);
	
	for(int i = 0; i < n - k + 1; i++){
		templist.clear();
		
		
		for(int j = i; j < k + i; j++){
			tt[0] = a[j];
			tt[1] = j;
			templist.push_back(tt);
		}
		sort(templist.begin(), templist.end());
		reverse(templist.begin(), templist.end());
		tempanswer = 0;
		temp = -1;
		
		
		
		for(auto v : templist){
			if(temp == -1){
				temp = v[1];
			}else{
				tempanswer += abs(temp - v[1]);
				temp = v[1];
			}
		}
		// for (auto i : templist) { 
		// 	for (auto j : i) { 
		// 		cout << j << " ";
		// 	}
		// cout << endl;
		// }
		// cout << "임시정답: " <<tempanswer << endl;;
		if(answer == -1){
			answer = tempanswer;
		}else{
			if(answer > tempanswer){
				answer = tempanswer;
			}
		}
		
	}
	cout << answer;
    return 0;    
}