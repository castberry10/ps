
/*
 * <최원영 202110579>
*/
// 32비트 정수를 2진수로 출력하는 함수
void print_binary(unsigned int num) {
    for (int i = 31; i >= 0; i--) {  // 31부터 0까지 반복
        putchar((num & (1 << i)) ? '1' : '0');  // 해당 비트가 1인지 0인지 체크
        if (i % 4 == 0) putchar(' ');  // 가독성을 위해 4비트마다 공백 추가
    }
    putchar('\n');
}

unsigned from_int_to_float(int x) {
  unsigned unsigned_x = 0;
  unsigned msb = (x >> 31) & 1;
  unsigned exp = 0;
  int cnt = 0;
  unsigned answer = 0;
  int pivot = 1;
  if(!x){ 
    return 0;
  }
  if(msb){ 
    x = ~x + 1;
  }
  while(cnt < 32){ 
    unsigned_x = unsigned_x | (pivot & x);
    pivot = pivot << 1;
    cnt += 1;
  }

  

  while(!(unsigned_x & (0x1 << 31))){
    exp += 1;
    unsigned_x = unsigned_x << 1;
  }

  unsigned_x = unsigned_x << 1;
  unsigned_x = unsigned_x >> 9;
  
  exp = (31 - exp) + 127;
  answer = msb << 31 | (exp << 23) | unsigned_x;  
  return answer;  
}
