import java.lang.*;
import java.io.*;
import java.util.*;
class PalindromeNumber{
	public static void main(String args[])throws IOException{
	int n,n1,remainder=0,reverse=0;
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter the number:");
	n=Integer.parseInt(br.readLine());
	n1=n;
	while(n>0){
		remainder=n%10;
		reverse=reverse*10+remainder;
		n=n/10;

	}
	if(n1==reverse){
		System.out.println(n1+" is a palindrome number");
	}
	else{
		System.out.println(n1+" is not a palindrome number");
	}
	}
}