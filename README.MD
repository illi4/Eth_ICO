# Correlation between the number of ICO on Ethereum blockchain and the number of transactions

## Summary

The goal of this project was to examine whether there was a correlation between the number of ICO on [Ethereum](https://ethereum.org/) blockchain and the number of transactions. 

Ethereum is an open-source, public, blockchain-based distributed computing platform featuring smart contract (scripting) functionality. Notably, the Ethereum token standard [ERC20](https://en.wikipedia.org/wiki/ERC20) is used for Ethereum smart contracts. Developed in 2015, ERC-20 defines a common list of rules that an Ethereum token has to implement, giving developers the ability to program how new tokens will function within the Ethereum ecosystem. This token protocol became popular with crowdfunding companies via Initial Coin Offering.

Initial Coin Offering (ICO) - an unregulated means by which funds are raised for a new cryptocurrency venture. An Initial Coin Offering (ICO) is used by startups to bypass the rigorous and regulated capital-raising process required by venture capitalists or banks. In an ICO campaign, a percentage of the cryptocurrency is sold to early backers of the project in exchange for legal tender or other cryptocurrencies. 

Over 2017, ICO received much of the blame for the Ethereum blockchain working slowly. 

The final visualisation available [here](https://illi4.github.io/Eth_ICO/) demonstrates how the growth in the number of ICO running on Ethereum has correlated with the load on the blockchain (number of transaction) starting from September 2016.
 
 ## Design 
 
For this visualisation, I have chosen a dual-axis bar chart as my goal was to show how the growth in one parameter correlates with the other over time. Initially, I tried looking at lines and scatterplots, but came back to the idea of bars as it looked more engaging and was easier to undesrtand. A number of changes have been made based on other's feedback, including: 

- Minor changes in colours
- Added animated text notes in the graph area 
- Added pause between the start of massive growth of the graphs and changed pauses (to larger) for bars growth 
- Changed period description from numerical to naming (e.g. 2017-01 to Jan-2017)
- Changed the formatting of the number of transactions (split with ',') 
- Added the 'pre-ICO' average dashed horizontal line     

First drafts are saved in the initial_versions folder: [index_0.1](initial_versions/index_0.1.html), [index_0.3](initial_versions/index_0.3.html).
 
## Feedback 

**First surveyed**
- Initial sketch: Seems like a good choice of visualisation type as we will be able to see growth of both over time. 
- First version: The colours are a bit pale, and there is a lot of stuff happening on the screen too fast. This is hard to follow.
- Final version: Looks much better. Really like the pauses and also the annotations. 

**Second surveyed**
- Initial sketch: Looks fine, but may be hard to understand for non-techies like myself. Could you add introductory information in the beginning of the page? 
- First version: It took me some time to understand what the numbers are (showing months) and what are the buttons appearing for. It is also hard to grasp when the numbers started growing quickly. 
- Final version: The final graph is easy to follow and navigate. 

**Third surveyed**
- Initial sketch: Would be worth trying other types of charts too (for example, scatterplot or line). Generally it looks fine. 
- First version: Looks beautiful, but the colour selection could be improved. Number formatting should be fixed in the descriptions (when clicking buttons). It is also not convenient that additional information appears below the chart when clicking the buttons. Generally, it is not quite clear why are these buttons needed for and it may seem that no information is displayed as it is below the chart. 
- Final version: Now it is easy to follow and understand. Additional improvements could be made with optimisation for mobile and scaling of SVGs. Also, em could be used instead of pixels in styles. 
 
## Resources

A dataset of Ethereum transactions (daily) from [Kaggle](https://www.kaggle.com/kingburrito666/ethereum-historical-data) was used. 
Information on Initial Coin Offerings was grabbed from [smithandcrown.com](https://www.smithandcrown.com/icos/#recent_completed).   
 
## Data files and data processing
The following files can be found in the repository: 
- [ICO_stats_initial_cleanup.csv](data_preparation/ICO_stats_initial_cleanup.csv): dataset with information on ICOs
- [tx.csv](data_preparation/tx.csv): dataset with information on transactions (daily)
- [convert.py](data_preparation/convert.py): python script used to process and wrangle data to create a final dataset for visualisation
- [tx_final_grouped.csv](data_preparation/tx_final_grouped.csv): final dataset with processed data
