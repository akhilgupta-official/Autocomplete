# Autocomplete
Autocomplete till 4 grams for SRM Search Engine. 




This module consist of four parts : 

1. Parsing : parsing the given paragraph in sets, where each set consist of four keyword.
	Here, i am using the data of duck duck go collected using duck_duck_go_hack.py

2. Indexing : Indexing the data in graph database, i am using Neo4j.
	graph database is selected to reduce redundancy of words as well as forming relation between words.

	Alternate, you can also use wordnet or word2vec for Autocomplete.

	The database of this module can also be used to in Name entity Recognition as well as in Natural Language Processing
	to understand the domain of the query asked by the user.

	for example :- Who is Apple CEO. 
				belongs to the technical domain.


3. Retrieval : Retrieving the words which form the relation with the previous given words.
	this module also consist of the autocorrect feature which will correct the incomplete last word given by the user,
	the autocorrect is based on keyboard (typing) errors.

4. Probability : Probability calculation of the words retrieved from the retrieval.py after doing autocorrect and the words which satify the relationship condition with the previous given words. 
	and arranging them in decreasing order of their probability.

	For three gram and four gram i have used Ordered Dictionary to give the more importance to the words which form a direct relationship with the previous given word.




