import java.lang.*;
import java.io.*;
import java.util.*;
class SelectionSort{
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
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++){
			if(a[i]>a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
	System.out.println("Sorted List:");
	for(i=0;i<n;i++){
		System.out.println(a[i]);
	}
	}
}