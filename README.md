# 1 Inverted Index
Given a set of documents, create an inverted index, which is a dictionary associating each word with a list of document identifiers where that word appears. The input is a 2-element list: [document id, text], where document id is a string representing a document identifier, and text is a string representing the content of the document. The text consists of space-separated words. The objective is to output the inverted index, where each word is associated with all its unique document identifiers.

## Input Format
- Each line contains two tab-separated elements.
- The first element is a string representing the document id.
- The second element represents the text in that document, consisting of space-separated words.

```
doc1 I love pasta
doc2 Italy is a great country having great Pasta
doc3 I love Italy because Italy has good Pasta
```

## Output format
In the output, each line starts with a word followed by a tab and a list of space-separated document ids associated with that word. The output needs to be sorted by the key (which is the word here)
```
a   doc2
because doc3
country doc2
good    doc3
great   doc2
has doc3
having  doc2
I   doc1 doc3
is  doc2
Italy   doc2 doc3
love    doc1 doc3
Pasta   doc2 doc3
pasta   doc1
```