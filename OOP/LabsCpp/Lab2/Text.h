#pragma once
#include <iostream>
#include "Line.h"
using namespace std;

class Text
{
public:
	Text();
	
	void AddLine(Line line);
	void ShowText();
	int GetLettersNumber();
	void RemoveLine(int index);
	void ClearText();
	int FindLine(Line line);
	void ReplaceChars(char ch1, char ch2);

private:
	Line* text;
	int SentenceCounter;
};

