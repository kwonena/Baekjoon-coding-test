#include <stdio.h>

int main() {
    int cnt;

    //cnt = 5;
    scanf("%d", &cnt);
    
    int a[cnt], b[cnt];

    // a와 b를 cnt만큼 입력 받는다
    for(int i = 0; i < cnt; i++) {
        scanf("%d %d", &a[i], &b[i]);
    }

    for(int j = 0; j < cnt; j++) {
        printf("sum : %d\n", (a[j] + b[j]));
    }
}
