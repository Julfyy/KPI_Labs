#pragma once
#include<cstring>
#include <string>

class Line
{
public:
	Line();

	Line(char* s);
	static Line InputLine(std::string s);
	char* GetSentence();
	int GetLength();
	bool IsEqual(Line line);
private:
	char* sentence;
	int sentenceLength;
	
};

