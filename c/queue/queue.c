#include <stdio.h>
#include <stdlib.h>

int queue[100], rear = -1, front = -1,choice, size,temporary;

int enqueue(){
    if(rear == size - 1){
        printf("\nQueue Is Full");
    }else{
        if(front == -1)
            front = 0;
        printf("Enter the element to queue: ");
        scanf("%d",&temporary);
        rear++;
        queue[rear] = temporary;
        printf("\nInserted value in queue is %d",temporary);
    };
};

int dequeue(){  
    if(front == -1){
        printf("The Queue is Empty");
        exit(1);
    }else{
        temporary = queue[front];
        front++;
         if(front > rear){
            front = rear = - 1;
        }
    };
};

int display(){
    if(front == -1){
        printf("The Queue is Empty");
        exit(1);
    }else{
        printf("The Queue is: ");
        for(int i=0;i <= rear;i++){
            printf("%d ",queue[i]);
        };
    };
};

int main(){
    printf("Enter the size of the queue: ");
    scanf("%d",&size);
    printf("Stack Using An Array");
    printf("\n\t--------------------------------");
    printf("\n\t 1.ENQUEUE\n\t 2.DEQUEUE\n\t 3.DISPLAY\n\t 4.EXIT \n\t");

    do{
        printf("\n\tEnter your choice: ");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
                break;
            default:
                printf("\n\tInvalid choice");
                break;
        }
    }while(choice!=4);
}   