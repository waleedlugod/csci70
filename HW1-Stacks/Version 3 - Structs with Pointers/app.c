#include <stdio.h>
#include "stack.h"

void application(){
    struct stack s0, s1;
    initstack(&s0);
    push(&s0, 'x');
    push(&s0, 'a');

    initstack(&s1);
    push(&s1, 'y');
    push(&s1, 'z');

    s1.top = 1;

    char ans = pop(&s1);
    printf("Popped from s1: %c \n", ans);
}

int main(){
    application();
    return 0;
}