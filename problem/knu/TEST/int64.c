#include <stdio.h>
#include <stdint.h>
#include <string.h> // memcpy 사용

int main() {
    long int var1;
    double var2;
    uint64_t bits_var1, bits_var2;

    printf("탐색 시작...\n");

    // long int의 가능한 모든 값을 탐색 (-2^63 ~ 2^63-1)
    for (var1 = INT64_MIN; var1 < INT64_MAX; var1++) {
        var2 = (double)var1; // var1을 double로 변환

        // long int 비트 패턴 가져오기
        bits_var1 = (uint64_t)var1;

        // double 비트 패턴 가져오기
        memcpy(&bits_var2, &var2, sizeof(var2));

        // 비트 비교
        if (bits_var1 == bits_var2) {
            printf("X = %ld: 같은 비트 표현을 가집니다!\n", var1);
            printf("var1 (long int) 비트: %016llX\n", bits_var1);
            printf("var2 (double) 비트:  %016llX\n", bits_var2);
            break; // 값을 찾으면 루프를 중단
        }
    }

    printf("탐색 완료.\n");
    return 0;
}
