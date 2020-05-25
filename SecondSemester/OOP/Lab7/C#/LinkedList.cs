using System;

namespace Lab7
{
    internal class LinkedList
    {
        private Node _head;

        public int Length
        {
            get
            {
                Node temp = _head;
                int lastIndex = 0;
                while (temp.Next != null)
                {
                    temp = temp.Next;
                    lastIndex++;
                }

                return lastIndex;
            }
        }

        public double MeanValue
        {
            get
            {
                short sum = 0;
                for (int i = 0; i <= Length; i++)
                {
                    sum += GetByIndex(i);
                }

                return (float) sum / Length;
            }
        }

        internal void InsertLast(short newData)
        {
            Node newNode = new Node(newData);
            if (_head == null)
            {
                _head = newNode;
                
                return;
            }

            Node lastNode = GetLastNode();
            lastNode.Next = newNode;
        }

        internal short GetByIndex(int index)
        {
            Node current = _head;
            int count = 0;

            while (current != null)
            {
                if (count == index)
                {
                    return current.Data;
                }

                count++;
                current = current.Next;
            }

            throw new IndexOutOfRangeException();
        }

        private Node GetLastNode()
        {
            Node temp = _head;
            while (temp.Next != null)
            {
                temp = temp.Next;
            }

            return temp;
        }

        public LinkedList()
        {
            _head = null;
        }

        public int GetNumberOfMultiples(int number)
        {
            int counter = 0;
            for (int i = 0; i <= Length; i++)
            {
                if (GetByIndex(i) % number == 0)
                {
                    counter++;
                }
            }

            return counter;
        }

        public void ReplaceWithZeroIfMoreThen(double value)
        {
            Node current = _head;
            while (current != null)
            {
                if (current.Data > value)
                {
                    current.Data = 0;
                }

                current = current.Next;
            }
        }

        public override string ToString()
        {
            Node current = _head;
            string stringArray = "";
            while (current != null)
            {
                stringArray += current.Data.ToString();
                stringArray += " ";
                current = current.Next;
            }

            return stringArray.Trim();
        }
    }


    internal class Node
    {
        internal short Data;
        internal Node Next;

        public Node(short data)
        {
            Data = data;
            Next = null;
        }
    }
}