#include <stdio.h>

int main(void) {
    int i1, i2;
    int cnt = 1;
    
    scanf("%d", &i1);
    scanf("%d", &i2);
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        for (int j = 1; j <= i; j++) {
            if (i1 <= cnt && cnt <= i2) {
                sum += i;
            }
            
            if (cnt > i2) {
                printf("%d", sum);
                return 0;
            }
            cnt++;
        }
    }
    return 0;
}