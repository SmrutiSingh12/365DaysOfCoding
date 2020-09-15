import java.lang.*;
import java.io.*;
import java.util.*;
class BinarySearch{
	public static void main(String args[])throws IOException{
	int a[]=new int[30];
	int n,i,j,temp,key,pos;
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter the size of array:");
	n=Integer.parseInt(br.readLine());
	System.out.println("Enter the array elements:");
	for(i=0;i<n;i++){
		a[i]=Integer.parseInt(br.readLine());
	}
	System.out.println("Enter the element to be searched :");
	key=Integer.parseInt(br.readLine());
	pos=bsearch(a,0,n-1,key);
	if(pos==-1)
		System.out.println(key+"is not found ");
	else
		
		System.out.println(key+"is found at"+pos);
	
	}
	public static int bsearch(int a[],int low,int high,int key)
	{
		int mid;
		mid=(low+high)/2;
		if(a[mid]>key)
		{
			high=mid-1;
		}
		else if(a[mid]<key)
		{
			low=mid+1;
					
		}
		else
		{
			return mid;

		}
		
		return -1;
	}
				
		
	
}