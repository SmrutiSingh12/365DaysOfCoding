#include<stdio.h>
#include<conio.h>
struct node
{ int data;
struct node *next;
}*top=NULL;

void push(int val)

{

	struct node *ptr;
	ptr=(struct node*)malloc(sizeof(struct node));
	ptr->data=val;
	if(top==NULL)
	{
		ptr->next=NULL;
		top=ptr;
	}
	else{
	ptr->next=top;
	top=ptr;
	}
}
void pop()
{
	struct node *ptr;
	if(top==NULL)
	{
		printf("Stack is empty");
	}
	ptr=top;
	printf("%d is deleted",ptr->data);
	top=top->next;
	free(ptr);
}

void display()
{
	struct node *ptr;
	ptr=top;
	if(top==NULL)
		printf("\n stack empty");
	else
	{
		while(ptr!=NULL)
		{
			printf("%d\n",ptr->data);
			ptr=ptr->next;
		}
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