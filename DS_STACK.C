#include<stdio.h>
#include<conio.h>
#define max 5
int top=-1;
int stack[max];
void pop()
{
	int val;
	if(top==-1)
	{
		printf("Stack is empty");
	}
	val=stack[top];
	printf("%d is deleted",val);
	top--;
}
void push(int data)
{
	if(top==max-1)
	{
		printf("Stack is overflow");
	}
	top++;
	stack[top]=data;
}
void display()
{
	int i;
	if(top==-1)
	{
		printf("Stack is empty");
	}
	for(i=top;i>=0;i--)
	{
		printf("%d\t",stack[i]);
	}
}
void main()
{
	int choice,data;
	clrscr();
	while(1)
	{
		printf("\n1.Push\t2.Pop\t3.Display\t4.Exit");
		printf("\nEnter the choice:");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:printf("Enter the value:");
			scanf("%d",&data);
			push(data);

			break;
			case 2:pop();

			break;
			case 3:display();
			break;
			case 4:exit(0);
			break;
			default:printf("Invalid choice");
			break;
		}
	}
	getch();
}