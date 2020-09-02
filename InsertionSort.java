import java.lang.*;
import java.io.*;
import java.util.*;
class InsertionSort{
	public static void main(String args[])throws IOException{
	int a[]=new int[30];
	int n,i,j,temp;
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
	int k=1;
	for(k=1;k<n;k++){
		temp=a[k];
		j=k-1;
		while((j>=0) && (temp<a[j])){
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=temp;
	}
	System.out.println("Sorted List:");
	for(i=0;i<n;i++){
		System.out.println(a[i]);
	}
	}
}