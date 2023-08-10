# Bible verse matcher
A small tool for linguists who are building corpora with bible texts.

There are bible translations for a huge amount of languages out there. Any linguists trying to work with these resources faces the problem how to arrange the data.
This python script concatenates two bible books that are translational equivalents and writes them to a single JSON file. It does so by matching up the two files verse by verse via the format given in the christian bible, e.g. 1:1 meaning paragraph 1, verse 1.

# How to use

```console:
python verse_matcher.py file1.txt file2.txt output.json
```
File 1 should be a text file with a book of the bible of your target language.
File 2 is a translational equivalent of the same file.

