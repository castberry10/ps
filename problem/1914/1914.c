#include <iostream> 
#include <cmath> 
#include <string>
#include <stdio.h> 
using namespace std;
int nf; 

void hanoi(int n, int from, int tmp, int to);

 int main(void) {
	scanf("%d", &nf);

	string a = to_string(pow(2, nf));

	int idx = a.find('.');

	a = a.substr(0, idx);

	a[a.length() - 1] -= 1;
	printf("%s\n", a.c_str());

	if (nf <= 20) {
		hanoi(nf, 1, 2, 3);
	}
	return 0;
}

void hanoi(int n, int from, int tmp, int to) {
	if (n == 1) {
		printf("%d %d\n", from, to);
	}
	else {
		hanoi(n - 1, from, to, tmp);
		printf("%d %d\n", from, to);
		hanoi(n - 1, tmp, from, to);
	}

}