#include <stdio.h>

int main() {
    int cnt = -1;
    
    int num[9];
    printf("Press nine number : ");
    for(int i = 0; i < 9; i++) {
        scanf("%d", &num[i]);
    }

    int max = num[0];

    for(int j = 0; j < 9; j++) {
        if(num[j] > max) {
            max = num[j];
        }
        cnt++;
    }
    printf("max : %d, cnt : %d\n", max, cnt);
}
