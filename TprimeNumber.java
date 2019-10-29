/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public final class TprimeNumber 
{
    static boolean isPrime(int n){
        if(n==2||n==3||n==5 || n==7||n==11){
            return true;
        }
        if(n%2==0||n%3==0||n%5==0||n%7==0)
            return false;
        for(int i=11;i*i<=n;i++){
            if(n%i==0)
                return false;
        }
        return true;
    }
    static boolean isTrimPrime(long n,boolean[] primes,int count){
        int sqrt=(int)Math.sqrt(n);
        if(primes[sqrt]==true && n==(long)sqrt*sqrt)
            return true;
        return false;
        
    }
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		boolean[] primes=new boolean[1000001];
		int count=1;
		primes[2]=true;
		
		for(int i=3;i<=1000000;i+=2){
		    if(isPrime(i))
		        primes[i]=true;
		}
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(br.readLine());
		String[] s=br.readLine().split(" ");
		int i=0;
		while(t>i){
		    if(isTrimPrime(Long.parseLong(s[i]),primes,count)){
		        System.out.println("YES");
		    }
		    else{
		        System.out.println("NO");
		    }
		    i++;
		}
		br.close();
	}
}

