# Interest Rate Risk
- Asset transformation function performed by financial institutions often exposes them to interest rate risk via the mismatching of asset and liability maturities.
- Financial institutions use two main methods to measure interest rate exposure.
	- **Repricing gap model** examines the impact of interest rate changes on a financial institution's net interest income.
	- **Duration gap model** incorporates the impact of interest rate changes on the overall market value of a financial institution's balance sheet and ultimately on its owners' equity or net worth.
- The Fed's monetary policy strategy is the most direct influence on the level and movement of interest rates.
	- If the Fed wants to slow down the economy, it will tighten the monetary policy by taking actions that raise the interest rates.
	- If the Fed wants to stimulate the economy, it allows the interest rates to fall.
- - -
# Repricing Model
- Repricing or funding gap is the difference between those assets whose interest rates will be repriced or changed over some future period **(RSAs)** and liabilities whose interest rates will be repriced or changed over some future period **(RSLs)**.
- It's a simple model used by small financial institutions in the US.
- It is essentially a book value accounting cash flow analysis of the interest income earned on a financial institution's assets and the interest expense paid on its liabilities over some particular period.
- The gap in each immaturity bucket is calculated by estimating the difference between the rate-sensitive assets and the rate-sensitive liabilities.
- The repricing model measures the change in a financial institution's net interest-income exposure to interest rate changes in each different maturity bucket.
- **A negative gap exposes the FI to refinancing risk**, which is the risk that the cost of rolling over or re-borrowing funds will rise above the returns being earned on asset investments.
- **A positive gap exposes the FI to reinvestment risk**, which is the risk that the returns on funds to be reinvested will fall below the cost of the funds.
$$ \Delta NII_i = (GAP_i)\Delta R_i = (RSA_i - RSL_i)\Delta R_i $$
- $\Delta NII_i =$ Change in Net Interest Income in the $i$th maturity bucket 
- $GAP_i=$ Dollar size of the gap between the book value of RSAs and RSLs in maturity bucket $i$
- $\Delta R_i=$ Change in the level of interest rates impacting assets and liabilities in the $i$th maturity bucket
- FI manager can also estimate cumulative gaps over various repricing categories or buckets.
$$ \Delta NII = \lparen \sum_{i = 1\text{ day}}^{1\text{ year}} RSA_i - \sum_{i = 1\text{ day}}^{1\text{ year}} RSL_i \rparen \Delta R_i = (CGAP)\Delta R_i$$