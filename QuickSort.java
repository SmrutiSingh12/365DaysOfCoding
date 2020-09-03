import java.lang.*;
import java.io.*;
import java.util.*;
public class QuickSort{
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
	quicksort(a,0,n-1);
	System.out.println("Sorted List:");
	for(i=0;i<n;i++){
		System.out.println(a[i]);
	}
	}
	 public static int partition(int a[], int beg, int end)  
    {  
          
        int left, right, temp, loc, flag;     
        loc = left = beg;  
        right = end;  
        flag = 0;  
        while(flag != 1)  
        {  
            while((a[loc] <= a[right]) && (loc!=right))  
            right--;  
            if(loc==right)  
            flag =1;  
            else if(a[loc]>a[right])  
            {  
                temp = a[loc];  
                a[loc] = a[right];  
                a[right] = temp;  
                loc = right;  
            }  
            if(flag!=1)  
            {  
                while((a[loc] >= a[left]) && (loc!=left))  
                left++;  
                if(loc==left)  
                flag =1;  
                else if(a[loc] <a[left])  
                {  
                    temp = a[loc];  
                    a[loc] = a[left];  
                    a[left] = temp;  
                    loc = left;  
                }  
            }  
        }  
        return loc;  
    }  
    static void quicksort(int a[], int beg, int end)  
    {  
          
        int loc;  
        if(beg<end)  
        {  
            loc = partition(a, beg, end);  
            quicksort(a, beg, loc-1);  
            quicksort(a, loc+1, end);  
        }  
    }  
}  