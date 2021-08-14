#include <stdio.h>

int main() {
    int cnt;

    printf("Press a number : ");
    scanf("%d", &cnt);

    for(int i = 0; i < cnt; i++) {
        for(int j = 0; j < cnt * 2 - 1; j++) {
            if((j < cnt - 1 - i) || (j >= cnt + i)) printf(" ");
            else printf("*");
        }
        printf("\n");
    }
    for(int i = 0; i < cnt; i++) {
        for(int j = 0; j < cnt * 2 - 1 - i; j++) {
            if(j < i) printf(" ");
            else printf("*");
        }
        printf("\n");
    }
}
