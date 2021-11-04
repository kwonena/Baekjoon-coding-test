// 약수
#include <stdio.h>

int main() {
    int cnt, answer = 1;

    printf("Press a number : ");
    scanf("%d", &cnt);

    int num[cnt];

    // 약수 입력
    printf("Press divisor number : ");

    for(int i = 0; i < cnt; i++) {
        scanf("%d", &num[i]);
        answer *= num[i];
    }
    printf("answer : %d", answer);
}
