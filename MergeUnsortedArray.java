import java.lang.*;
import java.io.*;
import java.util.*;
class MergeUnsortedArray{
	public static void main(String args[])throws IOException{
	int a[]=new int[20];
	int b[]=new int[20];
	int c[]=new int[20];
	int n1,n2,m,index=0,i;
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter the size of array1:");
	n1=Integer.parseInt(br.readLine());
	System.out.println("Enter the array elements:");
	for(i=0;i<n1;i++){
		a[i]=Integer.parseInt(br.readLine());
	}
	System.out.println("Enter the size of array2:");
	n2=Integer.parseInt(br.readLine());
	System.out.println("Enter the array elements:");
	for(i=0;i<n2;i++){
		b[i]=Integer.parseInt(br.readLine());
	}
	
	m=n1+n2;
	for(i=0;i<n1;i++){
		c[index]=a[i];
		index++;

	}
	for(i=0;i<n2;i++){
		c[index]=b[i];
		index++;

	}
	System.out.println("Merged Array:");
	for(i=0;i<m;i++){
		System.out.println(c[i]);
	}

	}
}