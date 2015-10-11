# potusScraper
Measuring presidential influence on foreign policy creation in Congress

### Introduction: An Experiment in Data Collection
This project experimented with data science techniques in collecting, analyzing, and communicating a foreign policy topic, thus presenting a new possibility for performing and displaying academic research.
Academic scholars have noted that the U.S. President can use speeches to both signal his own policy preferences and spur legislative debate on domestic policy. However, little attention had been placed on presidential speeches’ impact on foreign policy issues in the U.S. Congress. Here, I examined three key areas of foreign policy of recent relevance (2014-2015) in which the U.S. President has clearly indicated his intent for Congress to pass or to not pass some form of legislation:
  
  (1)	thawing relations with Cuba by lifting trade embargos;
  
  (2)	authorization of use of force against ISIL;
  
  (3)	and, ensuring that a negotiated agreement on Iran’s nuclear weapons program by preventing the passage of increased sanctions against Iran. 
  
### Hypotheses: Positive Signals Encourage, Negative Signals Dampen

My first hypothesis surmised that positive attention would lead toward positive outcomes:

*Hypothesis 1:* The more often the president speaks in favor of the passage of certain legislation (as measured by the number of speeches a president gives on a topic in a predefined, short time period), the more legislative activity around that topic will occur (as measured by number of bills introduced to Congress). 

Conversely, I tested the impact of negative attention on legislative activity, surmising that it would lead to a dampening effect on legislative activity:

*Hypothesis 2:* The more often a president speaks against the passage of certain legislation (as measured by the number of speeches a president gives on a topic in a predefined, short time period), the less legislative activity around that topic will occur (as measured by number of bills introduced to Congress).

### Summary of Results: Positive Signals Help, Negative Signals Harm

Presidential attention to the three foreign policy issues increased legislative activity around each respective topic. When President Obama sent positive policy signals—indicating he wanted a piece of legislation introduced to Congress—supporting legislation followed from members of his own party, and little to no directly opposing legislation was introduced by Republican members. However, when President Obama sent negative policy signals—indicating he did not want a piece of legislation introduced to Congress—opposing members introduced a flurry of legislation directly opposing his agenda. Each piece of legislation that directly supported or opposed the presidential agenda was introduced within a 30-day period of when the President spoke about one of the identified foreign policy topics.

### Methodology

First, I had to figure out how to measure presidential influence. I built on the academic concept of "going public," a term coined in 1986 by Samuel Kernell, who argued that presidents could improve their weak position of bargaining power with Congress by appealing to public opinion via broadcasted speeches. I counted how many times President Obama mentioned nine different words associated with each of the three foreign policy topics, identifying "clustering events" in which the president spoke more about a topic than at other times.

I used a bit of parallel processing to parse the speeches on the White House's website. The `WH_links` file pulls the links of each of the 10 speeches per every page of the archive and feeds them into each of the respective files in the `WH_workers` directory, which then count how many times a word appears per speech and output the results to a .csv file. Then, I used `getDailyValues` to total up these word counts per day instead of per speech.

Then, I had to figure out how to measure foreign policy activity in Congress. I decided to use legislative activity—the number of bills introduced to Congress—as a determination of support or opposition for the presidential agenda, identifying all the bills introduced that either supported or attempted to undermine the agenda set forth by President Obama on the three foreign policy topics identified above.

Again using parallel processing, the `Congress_links` directory pulls the links of each piece of legislation which is related to the respective foreign policy topic. The files in the `Congress_workers` directory then parse these links for desired information, like date of introduction, title of bill, and name and party of the member who proposed the bill.
