#include <iostream>
#include <string>

using namespace std;

/* Розбити на склади згідно з правилами перенесення слів
кожне слово на парній позиції у введеному з клавіатури рядку.
Визначити слова, перенесення яких неможливе.
*/


string getWord(string);
bool IsSpecSymbol(char);
string makeSyllables(string);
string Processing(string);
string cantBeMoved(string);

int main()
{

    cout << "Insert text" << endl;
    string text; // = "long time ago there was a man, who came out of the toilet and sing: Somebody once told me, the world is gonna roll me";
    getline(cin, text);

    cout << Processing(text) << endl;
    cout << "\nList of words that can`t be moved: " << cantBeMoved(text) << endl;
}

string getWord(string str)
{
    string word;
    int i = 0;
    char space = ' ';

    while (str[i] != space && i < str.length())
    {
        word += str[i];
        i++;
    }
    return word;
}

bool IsSpecSymbol(char letter)
{
    char l = tolower(letter);
    string a = "eyuioa";
    for (int i = 0; i < a.length(); i++)
        if (a[i] == l)
            return true;
    return false;
}

string makeSyllables(string word)
{
    string syll, splittedWord;
    int i = 0;

    while (i < word.length())
    {
        if (word.length() != 1)
        {

            if (IsSpecSymbol(word[i - 1]) && (word.length() - syll.length() > 1))
            {
                syll += "-";
            }
            syll += word[i];
            i++;
        }
        else
        {
            return word;
        }
    }

    return syll;
}

string Processing(string text)
{
    string word, splittedWord;
    int counter = 0;

    for (int i = 0; counter < text.length(); i++)
    {
        word = getWord(text.substr(counter, text.length()));

        if (i % 2)
            splittedWord.append(makeSyllables(word) + " ");
        else
            splittedWord.append(word + " ");

        counter += word.length() + 1;
    }
    return splittedWord;
}

string cantBeMoved(string str)
{
    string cantBeMovedWordsList, word;
    for (int i = 0; i < str.length(); i++)
    {
        word = getWord(str.substr(i, str.length()));
        i += word.length();

        if (word.length() <= 3)
            cantBeMovedWordsList.append(word + " ");
    }
    return cantBeMovedWordsList;
}
