import java.lang.*;
import java.io.*;
import java.util.*;
class PairMatching{
	public static void main(String args[])throws IOException{
	int a[]=new int[10];
	int n,i,j,temp=0,sum,flag=0;
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter the size of array:");
	n=Integer.parseInt(br.readLine());
	System.out.println("Enter the array elements:");
	for(i=0;i<n;i++){
		a[i]=Integer.parseInt(br.readLine());
	}
	System.out.println("Enter the desired sum no:");
	sum=Integer.parseInt(br.readLine());
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++){
			if(a[i]+a[j]==sum)
			{
				System.out.println(sum+" is the sum of "+a[i]+"+"+a[j]);
				flag=1;
			}
		}
	}
	if(flag==0){
		System.out.println(sum+" is not found as a sum of any elements");
	}
	
	}
}
/*
Enter the size of array:
5
Enter the array elements:
1
2
3
4
5
Enter the desired sum no:
5
5 is the sum of 1+4
5 is the sum of 2+3
*/