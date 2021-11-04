// 홀수
#include <stdio.h>

int main() {
    int num[7];
    int sum = 0;

    // 7개의 숫자 입력
    printf("Press seven number : ");
    for(int i = 0; i < 7; i++) {
        scanf("%d", &num[i]);
    }

    int min = num[6];

    for(int j = 0; j < 7; j++) {
        if(num[j] % 2 != 0) {
            sum = sum + num[j];
            if(num[j] < min) min = num[j];
        }
    }

    if(sum == 0) printf("-1");
    else {
        printf("sum : %d, min : %d", sum, min);
    }
}
