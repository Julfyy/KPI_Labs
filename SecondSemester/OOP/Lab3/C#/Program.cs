using System;
using System.Runtime.InteropServices.ComTypes;

namespace Lab3
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Text text = new Text(10);
            
            text.AddSentence("ayieuo");
            text.AddSentence("pppptrwqsdfghjklmnbvcxz");
            text.AddSentence("ay");
            

            Console.WriteLine(text[0]);
            Console.WriteLine(text[1]);

            Console.WriteLine(text._vovelsNumber);


        }
    }
}