### Spell-Checker: Wrote studying LeetCode 75 Problems

#### Introduction

Writing Spell-checker is a challenge due to the complicated nature of searching and matching correct matches of user written words. Thus, providing correct spellings. 

[StackOverflow](https://stackoverflow.com/questions/2294915/what-algorithm-gives-suggestions-in-a-spell-checker) and [Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance) offer in-depth knowledge in writing a spell-checker but are quite limited and outdated. It’s quite difficult to reverse engineer the spell checker ones present in Windows 11 by default. Including spell-checker has fundamental rules and later others tweak them to make it faster and add more features. 

Establishing no prior rules how it should work, and present Neural Spell Checkers being prominent in Grammarly and Google Docs, I went on quest to write a spell checker from scratch using my understanding of Algorithms specifically LeetCode problems I solved in the past couple of weeks and reading through Articles. 

#### Structure of SpellChecker

A unique and similar structure of past and present spell checkers were derived while designing this Algorithm. Starting 

1. A Prefix Tree search Algorithm to load every word from the dictionary into its respective nodes
2. Iterating over the words and using Longest Common Sequence (LCS) to find most likely match for the input word
3. Edit Distance (Levenshtein Distance) to determine the perfect match and returning result. 

Word with highest LCS and lowest Edit distance is determined as a perfect match. 

#### Learning outcomes

Practising LeetCode concepts in a real world project is valuable. Including better understanding how different Algorithms come into play and work to solve a critical problem in a unified manner. And showcasing problem solving and creativity traits. 

##### LeetCode Problems (used)
1. Edit Distance 
2. Longest Common Sequence 
3. Implement a Trie
4. Longest Common Prefix 

These were part of LeetCode 75 Problems. https://leetcode.com/studyplan/leetcode-75/

#### Catgeories of SpellChecker
1. Classical SpellChecker
2. Improved SpellChecker

**Classical SpellChecker:** (Edit Distance + Longest Common Sequence  + Prefix Trie)

**Improved SpellChecker:** (Hamming Distance + Longest Common Prefix + Longest Common Sequence + Prefix Trie

### Upgraded Features
1. Added Multiple types of SpellChecker
2. BERT next word predictor
3. LSTM next word predictor (Tensorflow trained model)
4. Embedding Spell Checker (experimental)

Embedding SpellChecker still in its infancy and does not provide a concrete alternative to pure Algorithm spellcheckers. Maybe there's some work in (logic) needed. 

I’ve added the model files and tokenizers on Hugging Face. In the repository, code for inference with the model can be found. Raise an issue if errors happen.

**Model Card: https://huggingface.co/sleeping4cat/Tensorflow-next-word-predictor**

##### Critical Pointers
1. I don’t provide UI and interface to interact with the algorithm. A terminal interface needs to be utilised. 
2. A Public dictionary dataset was used. 
3. The clearest explanation of Spell Checker Algorithm and Code on the Internet. 
4. Time Complexity O(n * m * (m + m))

**Consider star the repository if it helps you!**
