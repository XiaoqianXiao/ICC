# ICC
This script is originally generated for inter-rater reliability for RO1.\
Breifly, there are 3 models:\
ICC1: One-way random-effects model (target variance + error variance).\
ICC2: Two-way random-effects model; accounts for both targets and raters as random effects.\
ICC3: Two-way mixed-effects model; raters are treated as fixed.\
I used ICC3, since we are evaluating a specific rater, and the results apply to that specific rater, not a population of raters.\
Please refer [here](https://real-statistics.com/reliability/interrater-reliability/intraclass-correlation/intraclass-correlation-continued/) for more details of the models.\
\
For future usage, the rating report is suggested to save in the format with each column for one questionnaire. Refer the 'example.csv' for more details.
