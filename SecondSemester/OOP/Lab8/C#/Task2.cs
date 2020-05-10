namespace Lab8
{
    public static class Task2
    {
        public delegate int LineOperation(char symbol, string line);
        public static int GetCharIndex(char symbol, string line)
        {
            char[] charArray = line.ToLower().ToCharArray();
            for (int i = line.Length - 1; i >= 0; i--)
            {
                if (charArray[i] == symbol)
                {
                    return i;
                }
            }

            return -1;
        }
    }
}