# frequency_analysis_code_breaker
This code can break encrypted texts based on frequency analysis.
Once in a special maths class we learnt about the math behind encryption(Ceasar Cipher, RSA, etc.). At the end of the lesson, our teacher gave us 4 sentences, namely:
1. D ldsfxj qk d pxiiwn nhw ixsrk cwu hqk uyljxiid nhxs ghx kus qk khqsqsm, lug ndsgk qg ldtf ghx yqsugx qg lxmqsk gw jdqs lc ydjf gndqs.
2. Ycm imxw txl lmzmd sfdenzm. sfdenzmlmqq nq ycm xyydnbvym fs ycm qydfle.
3. Nxarncaensc nw xslh nxjsleace euac dcstbhmrh. Dcstbhmrh nw bnxnehm. Nxarncaensc hcgnlgbhw euh tslbm.
4. Skytlbt yusrptly hdot, prtytlbt yertlweutly ge.

In each sentence, every single character has been replaced by another character, same characters with the same other characters. The program decrypts these sentences by looping through the 1000 most common us english words and substitutes all appropriate matches for the original words. If a word matches (e.g. nhw - the), all characters are replaced with the characters of the new word. (e.g. n-t, h-h, w-e) The program runs until it has looped through the 1000 most common words and found all solutions. Note: if none of the words in your sentence are in the 1000 most common english words, the program fails, but this is very rare. Happy decrypting!

USAGE: run the python file freq_analysis_code_breaker.py and input your own, meaningful sentence / already encrypted sentence (type properly). Run the program. It may take some time to found some solutions since looping through so many words is time consuming. Note: Most solutions are gramatically not meaningful, but the words in them are all meaningful. US.txt contains more than 60 thousand english words and 1-1000.txt contains most common english words. 

File soutions.txt contains the solution for the 4 sentences, mentioned above. File example.txt contains an example, with the solution of the 1st sentence as input.
