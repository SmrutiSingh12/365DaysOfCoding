import java.lang.*;
import java.io.*;
import java.util.*;
class BubbleSort{
	public static void main(String args[])throws IOException{
	int a[]=new int[10];
	int n,i,j,temp=0;
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter the size of array:");
	n=Integer.parseInt(br.readLine());
	System.out.println("Enter the array elements:");
	for(i=0;i<n;i++){
		a[i]=Integer.parseInt(br.readLine());
	}
	System.out.println("Before Sorting:");
	for(i=0;i<n;i++){
		System.out.println(a[i]);
	}
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++){
			if(a[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
		}
	}
	System.out.println("Sorted List:");
	for(i=0;i<n;i++){
		System.out.println(a[i]);
	}
	}
}