# OpeningHandArchetypeEvaluator
This is an Opening Hand Archetypal Evaluator (OHAE). It sums the likelihood of drawing any of a given set of distributions of card archetypes from a deck without replacement.
The idea behind this was to create a means of quickly evaluating the likelihood that a given distribution of cards of a given set of archetypes, i.e. a "deck", would result 
in drawing "desireable distributions of opening hands", i.e. "keepable" opening hands. This is done by splitting the deck into archetypes of cards and creating a list of 
distributions of archetypes within your keepable hands, then using combinatorics to evaluate the portion of possible hands which satisfy those distribution metrics.

One example is the odds of drawing all of the same color &/or wildcards.
