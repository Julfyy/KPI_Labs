#include <iostream>
#include "Line.h"
#include "Text.h"


int main()
{
	

	Text text;
	
	text.AddLine(Line::InputLine("eeee"));
	text.AddLine(Line::InputLine("Hello world"));
	text.AddLine(Line::InputLine("It`s me"));
	text.AddLine(Line::InputLine("Bye"));
	

	
	text.ShowText();
	text.ReplaceChars('e', 'k');
	text.ShowText();

	return 0;
}