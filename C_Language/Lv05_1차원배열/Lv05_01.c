#include <stdio.h>

int main() {
    int cnt;

    // 정수의 개수 입력
    printf("Press a number : ");
    scanf("%d", &cnt);
    
    // 정수의 개수에 따라 숫자 입력
    int num[cnt];
    for(int i = 0; i < cnt; i++) {
        scanf("%d", &num[i]);
    }

    // 최대최소값 초기화
    int min = num[0];
    int max = num[0];

    // 최대최소값
    for(int j = 0; j < cnt; j++) {
        if(num[j] > max) {
            max = num[j];
        }
        if(num[j] < min) {
            min = num[j];
        }
    }
    printf("Max : %d\n", max);
    printf("Min : %d", min);
}
