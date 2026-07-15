#uni #s26 #bu419
# Lecture 05: Loss Reserving
---
### Terminology
- Insurer is the risk bearer. Could be an insurance company or a self-insurer.
- Reserves include future financial obligations for events that have already occurred.
	- Unpaid claim estimate is the result of the application of a particular estimation technique.
	- Carried reserve for unpaid claims is the amount reported in a published statement or in an internal statement of financial condition. 
- Loss is the economic loss sustained by the policyholder.
- Claim is the amount paid by the insurance company that covers their portion of the loss.
	- The policy holder might have a deductible or a policy limit, meaning the economic loss may be more than what the policy will pay.
---
### Claims Process
- The Claims process tracks a Claims timeline from the moment an accident happens to when the file is closed.
- This life cycle is what creates the lag between an event and its final payout.
- Let's understand this through an automobile policy example:
	- Assume an auto insurance policy was written on Jan 1, 2010, for one year.
	- An accident occurs on July 1, 2010. This is when the economic loss is sustained. It's called the accident date.
	- The insurer finally receives notice of the accident 8 months after it happened on March 1, 2011. This is called the report date.
	- Because the accident occurred in 2010 but wasn't reported until 2011, the company faced a financial statement liability on December 31, 2010, for a claim they didn't even know existed yet.
	- Once the claim is reported on March 1, 2011, a human insurance adjuster is assigned to the file.
		- The adjuster looks at the initial details and assigns a case reserve, also called case outstanding or case estimate.
		- The case reserve represents the estimated amount of money that is still outstanding to fully settle and close that specific claim.
		- As the claim progresses, the adjuster will continually update this number.
	- At any given evaluation date during the life of a claim, the total value known to the system is called the reported value. $$\text{Reported Value} = \text{Amount Paid to Date} + \text{Amount Out}$$
#### Ultimate claims
- It is the value of claims beyond which no other claims are expected.
- To derive an estimate of ultimate claims that are yet to be closed, an actuary looks years into the future to determine an estimated amount the insurer will pay when all claims have been settled and no further payments are anticipated.
- Ultimate claims consist of four components:
	1. Claim payments
	2. Case Outstanding for Claims that have Been Reported
	3. Development on case outstanding (IBNER: Incurred but not enough reserve)
	4. Claims that have been incurred but not yet reported (IBNYR)
- Total incurred but not reported $\text{IBNR} = \text{IBNER} + \text{IBNYR}$.
- Ultimate Claims:$$\text{Ultimate Claims} = \text{Cumulative Claim Payments} + \text{Case Outstanding} + \text{IBNR}$$
- Accurately estimating ultimate values is critical for running a P&C enterprise.
	- Recording proper claims, liabilities, and financial statements for events occurring on or before.
	- Making sure premiums are high enough to cover future ultimate costs.
	- Testing the insurers' prospective ability to meet long-term future obligations to policyholders.
- Unpaid Claims Reserve is the amount still outstanding on all the claims that have occurred on or before the statement date. $$\text{Reserve} = \text{Case Reserve} + \text{IBNR}$$ $$\text{Reserve} = \text{Ultimate Claims} - \text{Claims Paid-to-Date}$$
---
### Organizing the Data
- To find our ultimate cost and reserves, we first need a structured way to organize thousands of different claim transactions.
- Two primary ways to bucket this data:
	- Calendar your data:
		- Consider all loss transactions that occur during the 12-month calendar year without regard to the date of policy issuance, the accident date, or the reported date of the claim.
		- If a cheque is mailed out on November 5, 2026, it goes into the 2026 calendar year bucket, even if the car accident happened back in 2021.
		- Advantage: 
			- It is incredibly easy to get because companies track cash flow daily. Once a calendar year is over and the books are closed, that year's numbers never change.
		- Disadvantage:
			- It is useless for calculating results. Because it mixes old accidents with brand new accidents. It hides the true story line of how claims grow and mature over time. 
	- Accident year data 
		- Consider all lost transactions for claims that have an occurrence date during the year being evaluated, regardless of when the policy was issued or the claim was reported.
		- If a major accident happens on July 1, 2026, every single payment made for that accident over the next 5 or 10 years will always be sent back to the 2026 accident year bucket.
		- Advantage:
			- This allows actuaries to see the true life cycle of a specific group of claims.
		- Disadvantage:
			- There can be a temporary mismatch between the premium earned and the exposures during the evaluation window.
			- Most importantly, these buckets stay open for years, meaning the total cost for Accident Year 2026 will keep growing into the future.
---
### Development Triangle
- A development triangle is a table that shows changes in the value of various cohorts over time.
- Each row in the triangle represents one accident year.
- Each diagonal represents a successive valuation date.
- Each column in the claim development triangle represents an age or maturity and is directly related to the combination of accident year and valuation date used to create the triangle.
- Types of triangles exist to see different pieces of the puzzle:
	- Incremental paid: Shows exactly how much cash was paid out strictly inside that specific time window
	- Cumulative Paid: The running total of cash paid out up to that age.
	- Case estimates: The total value of adjusters' yet to be paid claims at that specific age.
	- Reported Claims: Calculated as **Cumulative Paid + Case Estimates**
	- Claim counts: Tracking the number of claims reported vs. closed.
---
### Importance of Unpaid Claims Reserves
- Reserves need to be accurately predicted so that the insurer remains financially sound, and products are priced appropriately.
- Under-reserving does not benefit policyholders because it threatens the ability of the firm to pay claims in the future.
- Over-reserving does not benefit the firm because it leads to higher premiums, and insureds pay too much for coverage, causing the insurer to not be competitive.
- Accurate reserving reduces volatility in profits.
---
### Development Method
- Key assumptions:
	- Ultimate claims for each accident year are produced from recorded values, assuming that future years' development is similar to prior years' development.
	- The underlying assumption in the development method is that claims recorded to date will continue to develop in a similar manner in the future.
	- The claims observed thus far tell you something about the claims yet to be observed.
- The development method consists of seven basic steps:
	1. Compile claims data in a development triangle
	2. Calculate age-to-age factors
	3. Calculate averages of the age-to-age factors
	4. Select Claim Development Factors
	5. Select Tail Factor
	6. Calculate cumulative claim development factors
	7. Project Ultimate Claims
- The actual example was done for an assignment, which I will attach later or as a separate PDF file along with these notes.
- When selecting factors, there can be a lot of different options that you could go for:
	- If the values are somewhat stable, then simple average tends to be used.
	- If the pattern has changed over time, then tend to rely on more recent years to capture the trend. This can be done by averaging over the last 3 or 5 years.
	- If the values are volatile, then tend to rely more on a weighted average or an average that excludes the highest and lowest values.
	- Typically, do not select a value that is based solely on the most recent one or two years unless there has been a change in the development pattern that is known and expected to continue in the future.
- A tail factor represents the development that is expected beyond the last maturity age in the available data.
	- Actuaries use several approaches to evaluate the tail factor.
	- For our purpose, we will use the simple method, (Bondy method) that just repeats the last factor.
- From the ultimate claims estimate, known reported, and paid claims, we can calculate our reserves:
	- **Unpaid Claims = Ultimate Claims Estimate - Paid Claims**
	- **Case Reserves = Reported Claims - Paid Claims**
	- **IBNR = Ultimate Claims Estimate - Reported Claims**
- When the development method works:
	- The primary assumption of this technique is that the reporting and payment of future claims will be similar to the patterns observed in the past.
	- Development method works best with a large volume of data.
	- It is particularly suitable for high-frequency, low-severity lines with stable and relatively timely reporting of claims.
---
### Adjustment Expenses
- Claim adjustment expenses are the costs of administering, determining coverage for, settling or defending claims, even if it is ultimately determined that the claim is invalid.
- Claim adjustment expenses are categorized as:
	- Allocated loss adjustment expenses
		- Correspond to those costs the insurer can assign to a particular claim, such as legal and expert witness expenses.
	- Unallocated loss adjustment expenses
		- Cannot be allocated to a specific claim. Examples include salaries, rent, and computer expenses for the claims department of an insurer.
- Just as there are unpaid claims, there are unpaid adjustment expenses associated with the claims that have yet to be paid.
- Therefore, we need a reserve for the outstanding portion of adjustment expenses as well.
- Allocated adjustment expenses are often included with claims as the development pattern is similar.
- Reserve for unallocated expenses is typically calculated separately.
---
### Reserve Accuracy & Data Concerns
- Recognize the impact of company policies.
- Impact of salvage and subrogation.
- Characteristics as claims evolve over time. Need to account for changes such as deductibles, limits, and reinsurance agreements.
- Credibility concerns.
- External factors including market conditions, legislative activities, inflation, catastrophes, and seasonality.
---
### Annual Return for P&C Companies
- Companies prepare a comprehensive annual return to accompany financial statements.
- The annual return includes Exhibit 60.35 for the claims and adjustment expenses paid in the current year, liabilities for incurred claims in the current year and prior year claims development.
