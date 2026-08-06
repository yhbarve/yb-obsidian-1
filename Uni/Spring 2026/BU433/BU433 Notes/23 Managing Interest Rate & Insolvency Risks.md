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
- Gap effect is the relation between changes in interest rates and changes in net interest income.
- - -
# Spread effect
- Spread effect is the effect that a change in the spread between rates on RSAs and RSLs has on net interest income as interest rates change.
$$ \Delta NII = (RSA \times \Delta R_{RSA}) - (RSL \times \Delta R_{RSL}) $$
- In general, the spread effect is such that, regardless of the direction of the change in interest rates, a positive relation exists between changes in the spread and changes in NII.
- When the spread increases, NII increases.
- - -
# Weaknesses of the repricing model
- It ignores market value effects of interest rate changes. Repricing gap is only a partial and short-term measure of overall interest rate exposure.
- It ignores cash flow patterns within a maturity bucket. On average, liabilities may be repriced towards the end of the buckets' range, and assets may be repriced towards the beginning.
- It fails to deal with the problem of rate-insensitive asset and liability cash flow run-offs and prepayments.
- It ignores cash flows from off-balance sheet activities.
- - -
# Duration Gap Model
- Duration measures the interest rate sensitivity of an asset or liability's value to small changes in interest rates.
$$ D = - \frac{\% \Delta \text{ in the market value of a security}}{\Delta R /(1+R)} $$
- Duration gap is a measure of overall interest rate risk exposure for an FI.
- To estimate the overall duration gap of an FI:
	- Determine the duration of an FI's asset portfolio and the duration of its liability portfolio.
	- Calculate the market value-weighted average of the duration of the assets or liabilities in the portfolio.
- The dollar change in the market value of the asset portfolio for a change in interest rates is: $$ \Delta A = A \times -D_A \times \frac{\Delta R}{(1 + R)} $$
- Similarly, the dollar change in the market value of the liability portfolio for a change in interest rates is: $$ \Delta L = L \times -D_L \times \frac{\Delta R}{(1 + R)} $$
- Re-arranging and combining these equations results in a measure of the change in the market value of equity. $$ \Delta E = -(D_A - kD_L) \times A \times \frac{\Delta R}{(1 + R)} $$
- Effect of interest rate changes on the market value of an FI's equity or net worth breaks down into three effects.
	1. Leverage Adjusted Duration Gap ($D_A - kD_L$)
	2. Size of the FI ($A$)
	3. Size of the interest rate shock ($\frac{\Delta R}{(1+R)}$)
- - -
# Difficulties in applying the duration model to real-world balance sheets
- **Duration matching can be costly.**
	- Critics claim that restructuring the balance sheet can be a time-consuming and costly process.
	- This argument isn't as true today, given the growth of purchased funds, asset securitization, and loan sales markets have eased the speed and lowered the transaction costs of major balance sheet restructurings.
- **Immunization is a dynamic problem.**
	- The duration of assets and liabilities changes as they approach maturity, and the rate at which their durations change through time may not be the same on the asset and liability sides.
- **Large Interest Rate Changes and Convexity**
	- **Convexity** is the degree of curvature of the price-yield curve around some interest rate level.
- - -
# Insolvency risk management
- Insolvency risk is the result or an outcome of excessive amounts of one or more of the risks taken by a financial institution. 
- To ensure survival, a financial institution manager must protect the institution against the risk of insolvency.
- The primary means of protection against the risk of insolvency and failure is an FI's equity capital.
- FI managers often prefer low levels of capital in order to generate a higher return on equity for stockholders.
- Capital Purchase Program was designed to encourage US FIs to build capital to increase the flow of financing to US businesses and consumers and to support the US economy.
- - -
# Capital
- The economic meaning of capital is net worth, which is the difference between the market value of an FI's assets and the market value of its liabilities.
- The market value or mark-to-market value basis uses balance sheet values that reflect current rather than historical prices.
- Regulatory and accounting defined capital and required leverage ratios are based in whole or in part on historical or book values accounting concepts.
## Market Value of Capital
- Decreases in current and expected future cash flows on assets lower the market value of the FI's asset portfolio.
- Decreases in the market values of assets are charged directly against the equity owner's capital or net worth.
- Liability holders are only hurt when losses on the asset portfolio exceed FI's net worth.
- Capital acts as insurance, protecting liability holders against insolvency risk.
- Rising interest rates reduce the market value of the FI's long-term securities and loans, while floating-rate instruments find their market values largely unaffected if interest rates on such securities are instantaneously reset.
## Book value of capital
- Book value of capital is the difference between the book value of assets and the book value of liabilities.
- A book value of capital usually comprises of the following three components:
	1. **Par value of shares:** The face value of the common shares issued by the FI times the number of shares outstanding
	2. **Surplus value of shares:** The difference between the price the public paid for common shares when originally offered and their par values, times the number of shares outstanding
	3. **Returned Earnings:** The accumulated value of past profits not yet paid in dividends to shareholders
- Book Value of Capital and Credit Risk:
	- Managers of FIs may resist writing down the values of bad assets as long as possible to try to present a more favourable picture to depositors, shareholders, and regulators.
	- FI managers can selectively sell assets to inflate their reported capital.
	- Only pressure from auditors and regulators may force loss recognition and write-downs of the values of problem assets.
- Book Value of Capital and Interest Rate Risk:
	- Failure of book value accounting systems to recognize the impact of interest rate risk is extremely relative to their partial and lagged recognition of credit risk problems.
## Discrepancy between the market and book values of equity
- Interest Rate Volatility: The higher the interest rate volatility, the greater the discrepancy.
- Examination and Enforcement: The more frequent are on-set and off-set examinations, and the stiffer the standards regarding charging off problem loans, the smaller the discrepancy.
- Asset trading: The more assets that are traded, the easier it is to access the true market value of the asset portfolio.
- **Market-to-book ratio** shows the discrepancy between the stock market value of a financial institution's equity and the book value of its equity.
- - -
# Arguments against Market Value Accounting
- Difficult to implement
	- Especially true for small commercial banks with large amounts of non-traded assets, such as small loans, in their balance sheets
	- When market prices or values for assets cannot be determined accurately, marking to market may be done only with error.
- Introduces unnecessary degree of variability into FI's reported earnings and thus net worth. This is because paper capital gains and losses on assets are passed through the income statement.
- FIs are less willing to accept longer-term asset exposures if these assets must be continually marked to market to reflect changing credit quality and interest rates.
- - -