namespace Lab5
{
    public class String
    {
        public string Sentence { get; protected set; }

        internal String(string str)
        {
            Sentence = str;
        }

        public int GetLength()
        {
            return Sentence.Length;
        }
    }
}