namespace Lab3
{
    public class Text
    {
        private Sentence[] _text;
        private static int _sentCounter;
        public int _vovelsNumber { private set; get; }

        void CountVovels()
        {
            string vovels = "eyuoai";

            for (int j = 0; j < _text[_sentCounter].sentence.Length; j++)
            {
                if (vovels.Contains(_text[_sentCounter].sentence.ToCharArray()[j]))
                {
                    _vovelsNumber++;
                }
            }
        }

        public Text(int n)
        {
            _text = new Sentence[n];
        }

        public void AddSentence(string sent)
        {
            _text[_sentCounter] = new Sentence {sentence = sent};
            CountVovels();
            _sentCounter++;
        }

        public int this[int index]
        {
            get => _text[index].sentence.Length;
        }
    }

    public class Sentence
    {
        public string sentence { get; set; }
    }
}