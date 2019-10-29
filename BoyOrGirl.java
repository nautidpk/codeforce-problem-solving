/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public final class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String strInput=br.readLine();
		int[] ch=new int[26];
		int count=0;
		for(int i=0;i<strInput.length();i++){
			int index=strInput.charAt(i)-'a';
			ch[index]++;
			if(ch[index]==1)
				count++;
		}
		if(count%2==0)
			System.out.println("CHAT WITH HER!");
		else
			System.out.println("IGNORE HIM!");
	}
}
