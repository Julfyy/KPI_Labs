using System;

namespace Lab5
{
    public class SymbolString : String
    {
        public SymbolString(string str) : base(str)
        {
            
        }
        public void Sort()
        {
            char[] temp = Sentence.ToCharArray();
            Array.Sort(temp);
            Array.Reverse(temp);
            Sentence = new string(temp);
        }
    }
}