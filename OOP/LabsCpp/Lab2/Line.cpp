#include "Line.h"

Line::Line() {}

Line::Line(char* s) {
	
	this->sentence = s;
}
Line Line::InputLine(std::string s)
{
    int len = s.length();
    char* p = new char [len + 1];

    for (int i = 0; i < len; i++) {
        p[i] = s[i];
    }
    p[len] = 13;
    

	Line line(p);
    
	return line;
}

bool Line::IsEqual(Line line)
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


char* Line::GetSentence() {
    return sentence;
}

int Line::GetLength()
{
    int lineLength = 0;
    for (int i = 0; sentence[i] != 13; i++)
    {
        lineLength++;
    }
    return lineLength;
}