#include <stdio.h>

int main() {

    printf("Number of sequences : ");
    int num;
    scanf("%d", &num);

    int set[num];

    printf("Comparison number : ");
    int x;
    scanf("%d", &x); // num보다 작아야 함

    for(int i = 0; i < num; i++) {
        set[i] = i + 1;
    }
    for(int j = 0; j < num; j++) {
        if(set[j] < x) printf("%3d", set[j]);
    }
}
