/* program to implement queue*/
#include<stdio.h>
#include<conio.h>
#define max 100
int queue[max];
int front=-1,rear=-1;
void insert(int val);
int delete_element();
int peep();
void display();
int main()
{int option,val;
  clrscr();
  do{
  printf("\n 1.Insert an element");
  printf("\n 2.delete an element");
  printf("\n 3.peek");
  printf("\n 4.Display");
  printf("\n 5.Exit");
  printf("\n enter your choice");
  scanf("%d",&option);
  switch(option)
  {  case 1:  printf("\n enter an element to insert");
	      scanf("%d",&val);
	      insert(val);
	      break;
     case 2:  val=delete_element();
	      if(val!=-999)
	      printf("\n value deleted is=%d",val);
	      break;
     case 3:  val=peep();
	      if(val!=-999)
	      printf("\n the first value in queue is=%d",val);
	      break;
     case 4:  display();
	      break;
     case 5: exit(0);
		break;
     default: printf("\n wroung option");

   }
   }while(option!=5);

  getch();
  return 0;
}
void insert(int val)
{ if(rear==max-1)
  { printf("\n overflow");
  }
  else
  {
   if(front==-1 && rear==-1)
   { front++; rear++;
   }
   else
   rear++;
   queue[rear]=val;
  }
}
int delete_element()
{int val;
    if(front==-1 || front>rear)
  { printf("\n underflow");
     val=-999;
  }
  else
  {
   val=queue[front];
   front++;
  }
  return val;

}
int peep()
{ int val;
 if(front==-1 || front>rear)
  { printf("\n underflow");
     val=-999;
  }
  else
  {
   val=queue[front];
  }
  return val;
}
void display()
{int i;
 if(front==-1 || front>rear)
  { printf("\n underflow");

  }
  else
  {printf("\n");
   for(i=front;i<=rear;i++)
   printf("\t%d",queue[i]);
  }
}
