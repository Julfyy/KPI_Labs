using System;

namespace ClassLibrary
{
    public class Line
    {
        private int _length;
        private char[] sentence;

        public char[] GetSentence()
        {
            return sentence;
        }

        public bool IsEqual(Line line)
        {
            bool isEqual = true;
            for (int i = 0; i < line.GetLength() && i < GetLength(); i++)
            {
                if (line.GetSentence()[i] != GetSentence()[i])
                {
                    isEqual = false;
                }
            }

            return isEqual;
        }

        public static Line InputLine()
        {
            char[] line = new char[1000];

            for (int i = 0; i < line.Length; i++)
            {
                line[i] = Console.ReadKey().KeyChar;

                if (line[i] == 13)
                    break;
            }

            Console.WriteLine();
            return new Line(line);
        }

        public Line(char[] sentence)
        {
            this.sentence = sentence;
        }

        public int GetLength()
        {
            int lineLength = 0;
            foreach (var i in sentence)
            {
                lineLength++;
                if (i == 13)
                    break;
            }

            _length = lineLength;
            return _length;
        }
    }


    public class TextShape
    {
        private Line[] _text;
        private int _sentenceCounter;

        public TextShape()
        {
            _text = new Line[100];
        }

        public void AddLine(Line line)
        {
            _text[_sentenceCounter] = line;
            _sentenceCounter++;
            Console.WriteLine("Lines: " + _sentenceCounter);
        }


        public void RemoveLine(Line line)
        {
            Line[] newText = new Line[100];
            int j = 0;
            for (int i = 0; i < _sentenceCounter; i++)
            {
                if (line.IsEqual(_text[i]))
                {
                    i++;
                    _sentenceCounter--;
                }

                newText[j] = _text[i];
                j++;
            }

            _text = newText;
        }

        public void ClearText()
        {
            for (int i = 0; i < _sentenceCounter; i++)
            {
                _text[i] = null;
            }
        }


        public int GetLettersNumber()
        {
            int sum = 0;
            for (int i = 0; i < _sentenceCounter; i++)
            {
                sum += _text[i].GetLength();
            }

            return sum;
        }

        public int findLine(Line line)
        {
            int count = 0;
            for (int i = 0; i < _sentenceCounter; i++)
            {
                if (line.IsEqual(_text[i]))
                {
                    count++;
                }
            }

            return count;
        }

        public void ShowText()
        {
            for (int i = 0; _text[i] != null; i++)
            {
                for (int j = 0; _text[i].GetSentence()[j + 1] != '\u0000'; j++)
                {
                    Console.Write(_text[i].GetSentence()[j]);
                }

                Console.Write(". ");
            }

            Console.WriteLine();
        }
    }
}