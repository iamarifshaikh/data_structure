#include <stdio.h>

int stack[100],top = -1, size, choice, temporary;

int push(){
    if(top >= size - 1){
        printf("Stack Is Overflow");
    }else{
        printf("\nEnter the element want to push in the stack");
        scanf("%d",&size);
        top++;
        stack[top] = temporary;
    };
};

int pop(){
    if(top <= -1){
        printf("Stack Is Underflow!");
    }else{
        printf("Poppped Element Is %d",stack[top]);
        top--;
    };
};

int display(){
    if(top >= 0){
        printf("Stack Elements Are: ");
        for(int i = 0;i <= top; i++){
            printf("\n%d",stack[top]);
        }
    }else{
        printf("Stack Is Empty!");
    }
};

int main(){
    printf("Enter the size of the stack: ");
    scanf("%d",&size);
    printf("Stack Operation Using An Array");
    printf("\n\t--------------------------------");
    printf("\n\t 1.PUSH\n\t 2.POP\n\t 3.DISPLAY\n\t 4.EXIT \n\t");

    do{
        printf("\nEnter your choice: ");
        scanf("%d",&choice);
        switch(choice){
            case 1:{
                push();
                break;
            }
            case 2:{
                pop();
                break;
            }
            case 3:{
                display();
                break;                
            }
            case 4:{
                printf("You reached the exit!");
                break;
            }
        }

    }while(choice != 4);
};