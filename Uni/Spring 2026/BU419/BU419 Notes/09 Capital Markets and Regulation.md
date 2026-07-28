# Capital Market Risk Financing
- Insurance companies use risk financing methods to smooth claims losses, cash flows, and for capital relief. Eg: Reinsurance
- Alternative risk financing brings in capital market products to handle these exact issues, especially for large-scale catastrophes.
- Capital market products are traded financial instruments with maturities greater than one year.
- When traditional reinsurance capacity drops or gets too expensive, capital markets offer a much larger pool of liquid capital.
- Traditional reinsurance still remains the primary foundation for most insurers. However, capital market products and catastrophe bonds are also used alongside to form a hybrid risk strategy.
- - -
# Insurance Linked Securities (ILS)
- An ILS is a financial instrument whose value is primarily driven by loss events. Its cash flows depend entirely on whether specific loss events occur.
- Because a hurricane or an earthquake doesn't care what the S&P 500 or interest rates are doing, ILS returns have a very low correlation with traditional stock and bond markets. This makes them attractive for institutional investors who are looking for true portfolio diversification.
- When an investor buys an ILS, their cash goes directly into a secure collateral account managed by the special purpose vehicle, usually invested in low-risk U.S. Treasury securities. So the investor receives two cash flows that form the total return:
	1. The interest earned on the safe treasuries in the collateral account
	2. An extra fee paid directly by the insurance company to the SPV for taking on their risk 
- In simple terms:
	- The investor acts like a reinsurer. They put up their cash to back potential catastrophe claims.
	- In return, the insurer gets paid for the risk. As long as no major disaster occurs, the investor keeps earning interest plus the premium paid by the insurer.
	- If a major disaster hits, the insurer uses the investor's money to cover claims.
- There are three primary parties involved, and here is how the mechanism works:
	1. The Ceding Insurer / Sponsor
		- It is the primary insurance company looking to offload its risk.
		- It transfers risk to the SPV via a financial contract.
		- It also pays a periodic insurance premium to the SPV to cover the cost of taking on that risk.
		- In the case of a qualifying catastrophic loss, it receives payouts from the SPV.
	2. The Special Purpose Vehicle (SPV)
		- It is an independent, legally isolated entity created solely to manage this specific securitization process.
		- It issues & sells catastrophe bonds to investors in the capital market.
		- It collects the cash from investors and puts them into a dedicated collateral account.
		- It combines the yield from the collateral account with the insurance premiums from the insurer to pay periodic coupon payments to investors.
		- If a catastrophe hits, the SPV liquidates the collateral to pay the insurer. If no catastrophe hits by maturity, it pays the principal back to investors.
		- The SPV is usually set up by the sponsor, but once set up, it is managed by a neutral third-party administrator, like a trust company or an investment bank. The government only steps in as a standard regulator to ensure that the SPV meets solvency and insurance compliance rules.
		- The insurer pays upfront setup legal and operational management fees to the SPV service providers. The SPV itself keeps 0% of the risk premium.
	3. Capital Market Investors
		- These are institutional investors like hedge funds, pension funds, and asset managers who buy catastrophe bonds.
		- They provide upfront capital (principal) to buy the ILS or CAT bond.
		- They receive high-yield interest payments during the bond's lifetime.
		- They act as a re-insurer in the sense that they assume the financial risk of losing a part or all of their principal if the trigger event occurs.
- - -
# Catastrophe Bonds
- This is the most common form of an ILS. It is designed specifically to protect insurers against high-severity, low-frequency disasters, using statistical models to set trigger standards.
- Bonds are issued by SPVs, developed and owned by large reinsurers, insurers, or large corporations, to serve as catastrophe bond intermediaries.
- Can be issued for any type of catastrophic insurable risk, including hurricanes, earthquakes, and other adverse weather and environmental risks.
- Payment to the insurer can be triggered in two main ways:
	1. Aggregate cat losses: Accumulation of multiple losses over a defined period.
	2. Single Event: A single massive event exceeding a set threshold
- Models are used to measure the frequency and severity probabilities that determine the standards used to measure the catastrophic risk embedded in these bonds.
- They are typically structured to provide protection against infrequently occurring events. (1-in-100-year to 1-in-250-year events)
	- Issue was like this because they get reliable financial protection against rare disasters that could threaten the existence of their firm at a predictable cost.
	- Investors also like this because of the ultra-low probability of occurrence, which means that they have a high statistical likelihood of collecting their full premium yield without losing their capital.
- - -
# Insurance Derivatives
- These are financial contracts whose value depends on the level of insurable losses or objective index measurements rather than physical assets. They offer faster and lower-cost risk management without setting up an SPV.
## Insurance Swaps
- Insurers exchange cash flow exposures to geographically diversify their risk portfolios.
- For example, Insurer A, who is facing heavy hurricane risk in Florida, swaps a portion of its potential payout stream with Insurer B, who is facing heavy tornado risk in the Midwest. Both offset their localized risk without raising external capital.
- If a hurricane hits Florida, insurer A will still be responsible for 100% of its policyholder's claims. However, because of the swap contract, insurer B will send cash to insurer A to cover the agreed-upon portion of the hurricane losses. Therefore, insurer A's net loss is reduced because insurer B absorbed a chunk of the bill. 
## Insurance Options
- This is a specialized type of option that derives its value from insurable losses or an objective index.
- For example, consider a basement repair contractor who is most profitable during unusually wet summers when cracks in basements are most likely to leak. Therefore, the worst-case weather situation for the contractor is a prolonged summer drought.
- The contractor determines that for every inch of precipitation shortfall below average for the months of August and September, the firm loses $10,000 in net income.
- To offset this risk, the repair contractor purchases a weather put option based on the measurement of rainfall during this period at the nearest weather station.
- The strike price is set at 5 inches. For every inch of precipitation below the strike value, the option increases in value by $10,000.
- The precipitation cover is written as an insurance policy and has a limit of $40,000. If the cumulative precipitation between August and September is only 3.5 inches, the contractor will receive a payout of $15,000 from the weather insurer to help offset any lost profit from a reduction in the demand for basement repair. 
- The put option is sold by a financial institution, a specialized broker or an insurance company, often called a weather insurer.
- They charge the contractor an upfront premium to write the option. They treat it like an underwriting risk - hedging it across a portfolio of weather contracts or taking the gamble that precipitation will stay above 5 inches.
- Advantages of insurance options:
	- Cheaper than ILS because there is no SPV to set up
	- Highly liquid and highly customizable.
	- Fast Settlement
- Disadvantages of insurance options:
	- High basis risk. In other words, the index payout might not perfectly match the actual financial loss.
		- A hurricane's wind speed at the nearest weather station might reach 130 mph and trigger a $50 million derivative payout. But if your specific insured properties suffered $80 million in flood damage from heavy rain, you are left with an unhedged $30 million loss. That discrepancy is **basis risk**.
	- Counterparty risk
	- Lower market liquidity compared to mainstream derivatives
- - -
# Financial Security & Basis Risk
- Traditional reinsurance has virtually zero basis risk and pretty high security. However, it is slow to settle and expensive to arrange.
- ILS and CAD bonds have high financial security with flexible trigger designs. They also have medium to low basis risk, depending on how the ILS is set up.
- Exchange-traded options have high security but very high basis risk because the index is broad and standardized.
- - - 
# Regulation
- Regulators require strict proof of actual risk transfer before granting capital relief.
- Regulators scrutinize parametric triggers and derivatives. If there is a significant basis risk, regulatory frameworks will limit or disallow full solvency capital credit because the insurer remains exposed to unhedged tail risk.
- Insurers must fully disclose SPV structures, collateral accounts, and counterparty exposures in regulatory filings.
- Regulators require proof that derivatives and swaps are used strictly for hedging existing insurance liabilities and not for speculative investment.
- - -
# Key Regulatory and Reporting Requirements for Alternative Risk Transfer (ART)
- Risk Transfer Requirements
	- To receive regulatory capital relief, the insurer must prove the ART mechanism transfers both underwriting risk and timing risk.
	- 