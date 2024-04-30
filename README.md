# short_bursts

*Update April 30, 2024*: The latest version of GerryChain has short bursts functionality. Best to use that. [Here it is applied to Louisiana State Senate](https://github.com/AustinLBuchanan/short_bursts/blob/main/gerrychain_shortbursts.ipynb).

Simple implementation of short bursts to generate Gingles demonstration plans

The short bursts framework comes from the following paper:
Cannon, Sarah, et al. "Voting rights, Markov chains, and optimization by short bursts." Methodology and Computing in Applied Probability 25.1 (2023): 36.

However, I have been unable to get the associated [code](https://github.com/vrdi/shortbursts-gingles/tree/main) to work. 

One of the authors pointed me to a subsequent implementation by Vedika Vishweshwar:
[code](https://github.com/vedikavish1/Georgia-Redistricting) [thesis](https://scholarship.claremont.edu/cmc_theses/2990/)

This is my attempt to simplify Vedika's code and apply it to Louisiana's tract-level graph. The code attempts to find as many Black-majority State Senate districts as possible while satisfying a +/-5% population deviation.

