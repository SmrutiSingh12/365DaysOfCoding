import java.lang.*;
import java.util.*;
import java.util.Arrays.*;

class AnagramJava{
	public static void main(String args[])
	{
		int i,j,flag=0;
		String temp,str1,str2;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the str1:");
		str1=sc.nextLine();
		System.out.println("Enter the str2:");
		str2=sc.nextLine();
		str1=str1.toLowerCase();
		str2=str2.toLowerCase();
		char a1[]=str1.toCharArray();
		Arrays.sort(a1);
		char b1[]=str2.toCharArray();
		Arrays.sort(b1);
		
		for(i=0;i<str1.length();i++)
			{
				if(a1[i]==b1[i])
				{
					flag=0;
				}
				else{
					flag=1;
					break;
				}
			}
		if(flag==0)
		{
			System.out.println("Strings are anagram");
		}
		else{
			System.out.println("String are not anagram");
		}

	}
}
/*
Output:
Enter the str1:
pwer
Enter the str2:
jhd
String are not anagram


Enter the str1:
Apple
Enter the str2:
Eppla
Strings are anagram
*/