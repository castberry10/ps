#include <stdio.h>
#include <stdint.h> 
#include <stdbool.h>  
#include <string.h>   

bool compare_8byte_char(char* stringa, char* stringb){
    return memcmp(stringa, stringb, 8) == 0;
}

double return_int_52_pow_of_2(){
    double temp = 4;
    temp *= 1024;
    temp *= 1024;
    temp *= 1024;
    temp *= 1024;
    temp *= 1024;
    
    return temp;
}
void print_longint(int64_t n) {
    int bits = sizeof(int64_t) * 8;  
    for (int i = bits - 1; i >= 0; i--) {
        printf("%ld", (n >> i) & 1);
    }
    printf("\n");
}

void print_double(double n) {
    unsigned char *p = (unsigned char*)&n;  
    for (int i = sizeof(double) - 1; i >= 0; i--) {  
        for (int j = 7; j >= 0; j--) {  
            printf("%d", (p[i] >> j) & 1);
        }
    }
    printf("\n");
}

int main() {
    double temp4 = 2;
    temp4 *= 1024;
    temp4 *= 1024;
    temp4 *= 1024;
    temp4 *= 1024;
    temp4 *= 1024;
    temp4 *= 512;
    
    double temp3 = 2;
    temp3 *= 1024;
    temp3 *= 1024;
    temp3 *= 1024;
    temp3 *= 1024;
    temp3 *= 1024;
    temp3 *= 64;

    double temp2 = 2;
    temp2 *= 1024;
    temp2 *= 1024;
    temp2 *= 1024;
    temp2 *= 1024;
    temp2 *= 1024;
    temp2 *= 256;
    
    double temp = 1024 * 1024 * 1024;
    temp *= 1024;
    temp *= 1024;
    temp *= 1024;
    temp *= 2;
    temp += temp2;
    temp += temp3;
    temp += temp4;
    
    int64_t a = (int64_t)temp; 
    double b = temp;
    print_longint(a);  
    print_double(b);
    return 0;
}