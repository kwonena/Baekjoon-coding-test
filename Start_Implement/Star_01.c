#include <stdio.h>

int main() {
    int cnt;

    printf("Press a number : ");
    scanf("%d", &cnt);

    for(int i = 0; i < cnt; i++) {
        for(int j = 0; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}
