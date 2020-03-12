#include "Text.h"

Text::Text() {
	text = new Line[100];
	SentenceCounter = 0;
}



void Text::AddLine(Line line) {
	text[SentenceCounter] = line;
	SentenceCounter++;
}

int Text::GetLettersNumber()
{
    int sum = 0;
    for (int i = 0; i < SentenceCounter; i++)
    {
        sum += text[i].GetLength();
    }

    return sum;
}

void Text::RemoveLine(int index)
{
    for (int i = index; i < SentenceCounter; i++)
    {
        text[i] = text[i + 1];
    }

    SentenceCounter--;
}



void Text::ClearText()
{
    for (int i = 0; i < SentenceCounter; i++)
    {
        text[i] = text[SentenceCounter];
    }
    SentenceCounter = 0;
}


void Text::ReplaceChars(char ch1, char ch2) {
    for (int i = 0; i < SentenceCounter; i++)
    {
        for (int j = 0; text[i].GetSentence()[j] != 13; j++)
        {
            if (text[i].GetSentence()[j] == ch1) {
                text[i].GetSentence()[j] = ch2;
            }
        }
    }
}



int Text::FindLine(Line line)
{
    int count = 0;
    for (int i = 0; i < SentenceCounter; i++)
    {
        if (line.IsEqual(text[i]))
        {
            count++;
        }
    }

    return count;
}


void Text::ShowText()
{
    for (int i = 0; i < SentenceCounter; i++)
    {
        for (int j = 0; text[i].GetSentence()[j] != 13; j++)
        {
            std::cout << text[i].GetSentence()[j];
        }

        std::cout << (". ");
    }

    std::cout << std::endl;
}