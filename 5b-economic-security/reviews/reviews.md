Review #144A
===========================================================================

Overall merit
-------------
3. Weak accept

Paper summary
-------------
The paper presents an emperical analysis of Compound, an Ethereum based blockchain for borrowing in cryptocurrency to gain assets (PLF: protocol for loanable funds).  The paper presents the data about the amount of funds going around in Compound.  It is a well-written, light-weight paper, without great new contributions but of definite interest.

Comments for author
-------------------
The paper is well written, and the concepts otherwise infamilair to a computer scientists are very clearly explained. 

The results are clear, perhaps not surprising, but especially interesting is the impact of the governance token.  

- [ ] There is no discussion about the future of such PLF systems, or the limitations or dangers of such PLF. It seems there is a lot of room for discussion, eg about the implications of the governance token, both from a financial perspective and from that of the associated risk taking.

Justification of recommendation
-------------------------------
- [ ] A smallish contribution, looking at emperical data of the Compound PLF (borrowing system on the blockchain). Very accessible for non-economist or non-finance people.



Review #144B
===========================================================================

Overall merit
-------------
2. Weak reject

Paper summary
-------------
Provides a summary on loanable funds with a particular focus on Compound and liquidations. They highlight that the top 10 accounts are responsible for a significant portion of the lending/borrowing. It identifies the spike of deposits around the change of the COMP token dynamics (e.g. reward borrow/lend equally).

Comments for author
-------------------
I feel like the background could be condensed / shorter.

- [ ] You could have three sections:
- Ethereum
- Collateral types (ERC20, Stablecoins)
- Loanable Funds (Collateralisation, Overview, Oracles, Liquidity Incentives)

- [ ] It should save on the heading space. Potentially Loanable Funds could be its own section. 

There are some interesting finds about the top 10 users who borrow / supply compound. 
- [ ] I think the authors should distinguish if the top 10 users are EOA (signing keys) or smart contracts. If it is the latter, then it would be good to know what that smart contract is doing (e.g. is it something like PoolTogether that combines all funds into it?). I'd be very surprised if it is strictly EOA and we shouldn't accept the paper until this is confirmed (because it has implications on how quantity of real users). 
- [ ] If page limit permits, I'd also propose a table of the addresses + amounts + percentages. 

- [ ] The 3% decrease to trigger liquidations has me a bit confused. Is it the DAI peg (Dollar/DAI) that could decrease by 3%? Or ETH relative to DAI? If the former, it makes sense. If the latter, then there are crazy swings per day of more than 3% so how has this not been triggered yet? It would be nice to clarify this in the paper.

Justification of recommendation
-------------------------------
Generally speaking, its a measurement of the compound protocol in terms of borrowing, lending, and liquidations. It mostly relies on data generated via smart contract events, followed by an explanation of how compound works. I found the paper interesting to learn more about compound, but I am not sure if there are many new insights in the paper itself or if any research questions have been answered. For that, I'm leaning towards a weak reject and I would recommend it for the workshop.



Review #144C
===========================================================================

Overall merit
-------------
2. Weak reject

Paper summary
-------------
This paper looks at lending protocol in defi (PLFs) and in particular proposes a model for representing their internal state as well as performs a case study of the Compound protocol and the liquidations that have occurred there. The model is also used to perform a sensitivity analysis that evaluates the liquidations that would occur for a hypothetical deviation in the value of any of the tokens in the PLF markets.

Comments for author
-------------------
- [ ] One of the big things that I was looking for which was not present here is an analysis of the users who cycle their lends and borrows in Compound. Essentially what people do is they deposit some collateral and then draw the maximum loan size against it, then they take that loan and feed it back in as additional collateral and draw another loan against that. In this way. In this way, an initial deposit of say 100 Dai can turn into 100*(1/(1-borrow_factor)) Dai. I believe Dai markets allow users to borrow 75% of the value of their collateral, so they effectively can leverage their initial deposit 4x. This is a huge part of why the borrow rates are as high as they are, and this hidden leverage factor is responsible for a lot of phenomena like the Dai used as collateral in Compound is over 2x the entire market capitalization of Dai. 

- [ ] Another thing that I would like to see is how the model is applicable to other PLFs. I know that most of these PLFs are structurally basically the same thing, but it would be good in the paper to know that this model will likely generalize to many different markets. 

- [ ] I like the discussion around the behavior of users changing in response the the additional incentives from the COMP token being launched. In addition to just monitoring liquidations though, I think it would be been good to expand on Figure 4 and talk about the general posturing of users, and actually use the price of COMP to look at how incentivized they were to take those risks. Also, I wouldn't look at just sensitivity to the price of Dai since Dai is for the most part relatively stable and people's expectations about future Dai prices are very different from other assets. Instead of I would consider what happens when a borrower's liabilities or a lender's collateral changes because it is ETH or something. 

- [ ] I found Figure 3 to be really confusing. Typically for a cumulative distribution, the X-Axis is a sorted list of users, and the Y-axis is the sum of funds that come from users <= x for a point(x,y). Also the numbers on the Y-axis were not round and it was hard to read. It might also be a good idea to make the Y-axis log scale.

Justification of recommendation
-------------------------------
I like the topic, and I like the goal of the paper which is to develop a framework for analyzing PLFs in addition to a case study of Compound. I feel that in this case, the execution is a bit weak, namely its not clear that the framework is generalizes, and some really important aspects of understanding Compound were overlooked.



Review #144D
===========================================================================

Overall merit
-------------
3. Weak accept

Paper summary
-------------
An analysis of the current behavior of the Compound DeFi scheme...

Comments for author
-------------------
Overall an interesting analysis of "what" is going on in the Compound DeFi scheme: the rate of loans, the prevelence of whales, the time between an oracle indicating an instance is ripe for liquidation and when it is liquidated.

- [ ] The latter, on efficiency of liquidation, could use some further examining.  In particular is there any evidence of mining-pool-driven front running in the liquidation events?  There is evidence that there are automatic Ethereum front runner bots that cooperate/are integrated into the mining pools, and this looks like a ripe target for such bots.  Can you examine to see if that is happening?  In particular are there some particularly effective hunters who's liquidations are only seen in some mining pool blocks?

- [x] I also really wish there was an analysis of "why" however: what is the point of Compound is overall?  It can be used to increase leverage (especially with recursive inclusion) but even then it isn't much.  Given the huge amount outstanding vs the actual low level of liquidations and huge amount of overcollateralization after the addition of the COMP token, how much of the activity is simply recircular collateralization/borrowing simply to farm the increasing supply of COMP tokens as a speculative vehicle for cryptocurrencies not otherwise trading.

- [ ] The massive, MASSIVE surge when the COMP token was introduced seems to strongly suggest the behavior is not because of the utility of Compound per se but the desire to acquire COMP tokens.  This could clearly be seen if you augment figure 4 with a version that is % of outstanding: the 150% to >2x overcollateralization is strongly correlated with the COMP token, while razor thin overcollaterization would be an indication of speculative leverage.

Justification of recommendation
-------------------------------
A data analysis of Compound showing in particular the effects of liquidation, overcollateralization, and the creation of the COMP token.