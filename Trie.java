/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

public final class Trie{
    char[] ch;
    Trie[] tr;
    int[] count;
    Trie(){
        ch=new char[26];
        count=new int[26];
        tr=new Trie[26];
    }
    static String insertIn(String s,Trie root){
        int n=s.length();
        for(char c:s.toCharArray()){
            n--;
            int index=c-'a';
            if(root.ch[index]==c){
                
            }
            else{
                root.ch[index]=c;
            }
            if(n==0){
                root.count[index]++;
                if(root.count[index]>1){
                    return s+(root.count[index]-1);
                }
                else
                return "OK";
            }
            if(root.tr[index]==null){
                root.tr[index]=new Trie();
            }
            root=root.tr[index];
        }
        return "OK";
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        Trie t=new Trie();
        while(n-->0){
            Trie root=t;
            String s=br.readLine();
            String ans=insertIn(s,root);
            System.out.println(ans);
        }
    }
}
