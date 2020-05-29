# banxico_analyser

Banking on an earlier developed project, we aim to use natural language processing techniques to analyze every monetary policy statement that the Bank of Mexico (Banxico) has issued with regards to its monetary poliy stance (whether it raised, lowered or mantain unchanged its key policy rate). By doing so we expect to extract the frequency with which key words or groups of words (binominal, trinomial, etc) are used and extract a correlation between these counts and market fluctuations in response to them as well as between the counts and future policy decisions. 

We will be using python to transform the statements into processable text files, matplotlib and numpy to create the relevant indicators, correlations and graphs, and, as said, NLP to derive word ferquencies. Besides the statements, we have data on market interest rates and Banxico's policy rate readily available in Banxico's API. 
