// 이진수
#include <stdio.h>

int main(void)
{
    int num, originNum, cnt, mok, nmg;
    int arr[10];

    printf("Please enter a number : ");
    scanf("%d", &num);

    originNum = num;
    cnt = -1;

    while(1) {
        cnt++;
        mok = (int)num/2;
        nmg = num - mok*2;
        arr[cnt] = nmg; // 거꾸로 출력해야함
        
        if(mok == 0) { 
            printf("originNum : %d\n", originNum);
            for(int i = 0; i <= cnt; i++) {
                if(arr[i] == 1) {
                    printf("%3d", i);
                }
            }
            break;
        }
        num = mok;
    } 
}