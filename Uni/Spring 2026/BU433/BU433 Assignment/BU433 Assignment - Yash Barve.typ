// --- frontmatter ---
#let title = "Motivation"
#let fm = (
  "title": "Motivation",
)

#set page(
  paper: "a4",
  margin: (x: 2.5cm, y: 3cm),
  header: context {
    if counter(page).get().first() > 2 {
      set text(size: 9pt, fill: luma(120))
      line(length: 100%, stroke: 0.4pt + luma(180))
      v(-8pt)
      align(right)[#fm.at("title", default: "")]
    }
  },
  footer: context {
    if counter(page).get().first() > 2 {
      set text(size: 9pt, fill: luma(120))
      align(center)[#counter(page).display("1 / 1", both: true)]
    }
  },
)
#set text(font: ("Verdana", "Arial", "Liberation Sans"), size: 11pt)
#set heading(numbering: "1.1.")
#set table(stroke: 0.5pt)
#show figure: set block(below: 1.5em)

#let _co-colors = (
  "note":      (fill: rgb("#dbeafe"), accent: rgb("#1d4ed8")),
  "info":      (fill: rgb("#dbeafe"), accent: rgb("#1d4ed8")),
  "tip":       (fill: rgb("#dcfce7"), accent: rgb("#15803d")),
  "hint":      (fill: rgb("#dcfce7"), accent: rgb("#15803d")),
  "important": (fill: rgb("#dcfce7"), accent: rgb("#15803d")),
  "warning":   (fill: rgb("#fef9c3"), accent: rgb("#a16207")),
  "caution":   (fill: rgb("#fef9c3"), accent: rgb("#a16207")),
  "attention": (fill: rgb("#fef9c3"), accent: rgb("#a16207")),
  "danger":    (fill: rgb("#fee2e2"), accent: rgb("#b91c1c")),
  "error":     (fill: rgb("#fee2e2"), accent: rgb("#b91c1c")),
  "bug":       (fill: rgb("#fee2e2"), accent: rgb("#b91c1c")),
  "quote":     (fill: rgb("#f1f5f9"), accent: rgb("#475569")),
  "cite":      (fill: rgb("#f1f5f9"), accent: rgb("#475569")),
)
#let _co-icon-paths = (
  "note":      "<circle cx='12' cy='12' r='10'/><line x1='12' y1='16' x2='12' y2='12'/><line x1='12' y1='8' x2='12.01' y2='8'/>",
  "info":      "<circle cx='12' cy='12' r='10'/><line x1='12' y1='16' x2='12' y2='12'/><line x1='12' y1='8' x2='12.01' y2='8'/>",
  "tip":       "<path d='M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5'/><path d='M9 18h6'/><path d='M10 22h4'/>",
  "hint":      "<path d='M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5'/><path d='M9 18h6'/><path d='M10 22h4'/>",
  "important": "<circle cx='12' cy='12' r='10'/><line x1='12' y1='8' x2='12' y2='12'/><line x1='12' y1='16' x2='12.01' y2='16'/>",
  "warning":   "<path d='m21.73 18-8-14a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3'/><line x1='12' y1='9' x2='12' y2='13'/><line x1='12' y1='17' x2='12.01' y2='17'/>",
  "caution":   "<path d='m21.73 18-8-14a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3'/><line x1='12' y1='9' x2='12' y2='13'/><line x1='12' y1='17' x2='12.01' y2='17'/>",
  "attention": "<path d='m21.73 18-8-14a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3'/><line x1='12' y1='9' x2='12' y2='13'/><line x1='12' y1='17' x2='12.01' y2='17'/>",
  "danger":    "<path d='M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z'/>",
  "error":     "<circle cx='12' cy='12' r='10'/><path d='m15 9-6 6'/><path d='m9 9 6 6'/>",
  "bug":       "<path d='m8 2 1.88 1.88'/><path d='M14.12 3.88 16 2'/><path d='M9 7.13v-1a3.003 3.003 0 1 1 6 0v1'/><path d='M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6z'/><path d='M12 20v-9'/><path d='M6.53 9C4.6 8.8 3 7.1 3 5'/><path d='M6 13H2'/><path d='M3 21c0-2.1 1.7-3.9 4-4'/><path d='M20.97 5c0 2.1-1.6 3.8-3.5 4'/><path d='M22 13h-4'/><path d='M17 17c2.3.1 4 1.9 4 4'/>",
  "quote":     "<path d='M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z'/><path d='M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z'/>",
  "cite":      "<path d='M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z'/><path d='M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z'/>",
)
#let callout(kind, title, body) = {
  let c = _co-colors.at(kind, default: (fill: rgb("#f3f4f6"), accent: rgb("#374151")))
  let paths = _co-icon-paths.at(kind, default: none)
  let hdr = context {
    if paths != none {
      let cap_h = measure(text(fill: c.accent, weight: "bold")[H]).height
      let svg = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='" + c.accent.to-hex() + "' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'>" + paths + "</svg>"
      box(height: 1.5 * cap_h, baseline: 1.5 * cap_h / 12, image(bytes(svg), format: "svg")) + h(4pt) + title
    } else { title }
  }
  block(fill: c.fill, inset: (x: 12pt, y: 10pt), radius: 4pt, width: 100%)[
    #text(fill: c.accent, weight: "bold")[#hdr] \
    #body
  ]
}

#page(margin: (x: 2.5cm, y: 3cm), header: none, footer: none)[
  #let _t  = fm.at("title",    default: "")
  #let _st = fm.at("subtitle", default: "")
  #let _au = fm.at("author",   default: "")
  #let _dt = fm.at("date",     default: "")
  #let _vs = fm.at("version",  default: "")
  #let _ss = fm.at("status",   default: "")
  #let _su = fm.at("summary",  default: "")
  #v(1fr)
  #if _t != "" [
    #text(size: 28pt, weight: "bold", fill: rgb("#1e3a5f"))[#_t]
    #if _st != "" [
      #v(0.3cm)
      #text(size: 16pt, fill: rgb("#2c5282"))[#_st]
    ]
    #v(0.6cm)
    #line(length: 100%, stroke: 1.5pt + rgb("#1e3a5f"))
    #if _su != "" [
      #v(0.4cm)
      #block(stroke: (left: 3pt + rgb("#1e3a5f")), inset: (left: 12pt, y: 6pt))[#_su]
    ]
    #v(1fr)
    #grid(
      columns: (1fr, 1fr),
      row-gutter: 0.4em,
      [#if _vs != "" [*Version:* #_vs]], [#if _au != "" [*Author:* #_au]],
      [#if _dt != "" [*Date:* #_dt]],    [#if _ss != "" [*Status:* #_ss]],
    )
  ] else [
    #text(size: 16pt, fill: luma(120))[_No title found._]
    #v(0.4cm)
    #text(size: 10pt, fill: luma(120))[
      Add frontmatter to your document to populate this cover page. \
      Supported fields: `title`, `subtitle`, `author`, `date`, `version`, `status`, `summary`. \
      See the README for details.
    ]
    #v(1fr)
  ]
  #v(0.5cm)
]

#outline(indent: 1em)

#pagebreak()

The choice of Capital One Financial Corporation (Capital One, COF) was driven by its industry-level strategic significance. Although it is legally and functionally a bank holding company, it operates like a technology company.

Capital One is among the few financial institutions that did not evolve from a legacy brick-and-mortar footprint. Instead, it was founded on an "Information-Based Strategy". At Capital One, cloud infrastructure, real-time data analytics, risk-based pricing and software engineering directly drive credit underwriting and customer acquisition.

From an institutional management perspective, Capital One offers a compelling case study in balancing high-yield consumer credit risk with a massive retail deposit base (\$475B+) that lowers funding costs.

#line(length: 100%)

= History & Corporate Evolution

Capital One was co-founded by current CEO Richard Fairbank and Nigel Morris in 1988. They conceived a data-driven approach to consumer lending, and pitched their concept of Information-Based Strategy to Signet Bank based in Richmond, Virginia. Signet adopted the model and launched its credit card division under the leadership of Fairbank and Morris. Following rapid growth, in 1994, Signet spun off its credit card division as an independent entity and formally named it Capital One. The firm officially went public in early 1995. _(Clemons & Thatcher, 1998)_

Originally operating solely as a credit card lender, the company pioneered customized interest rates and balance-transfer offers using predictive data modelling. Capital One recognized the risk of relying solely on unsecured credit card lending. The company therefore executed a multi-decade diversification strategy through major strategic acquisitions, including:

- Hibernia National Bank (2005)
- North Fork Bank (2006)
- Chevy Chase Bank (2009)
- ING Direct USA (2012)
- HSBC's US credit card portfolio (2012)

Most recently, in 2024-2025, Capital One executed a \$35.5 billion acquisition of Discover Financial Services, creating one of the largest consumer banking and payments platforms in North America and acquiring its own proprietary payment network. _(Capital One Financial Corp., 2024)_

#line(length: 100%)

= Organizational Structure

Capital One Financial Corporation is organized as a Bank Holding Company (BHC) and a Financial Holding Company (FHC) under the US Bank Holding Company Act of 1956. It operates through two primary insured depository subsidiaries:

1. *Capital One, National Association (CONA):* The primary national banking subsidiary that houses the firm’s retail deposit-gathering network, branch operations, auto finance business, and commercial lending divisions.
2. *Capital One Bank (USA), National Association (COBNA):* The specialized credit card bank subsidiary that issues domestic consumer and small business credit cards, alongside certain instalment loan products. Corporate Governance is centralized at the holding company level in McLean, Virginia. _(Capital One Financial Corp., 2025)_

#line(length: 100%)

= Products & Services Offered

Capital One organizes its financial products and services into three reportable business segments:

1. *Credit Card:* The Credit Card segment is Capital One’s primary revenue driver, generating income via net interest margins on revolving card balances and interchange fees from transaction processing.
2. *Consumer Banking:* The Consumer Banking segment provides foundational retail banking services, serving as Capital One’s primary engine for low-cost deposit funding.
3. *Commercial Banking:* The Commercial Banking segment caters to middle-market corporations, commercial real estate developers, and institutional clients. _(Capital One Financial Corp., 2025)_

#line(length: 100%)

= Geographic Footprint

Capital One operates through a hybrid digital-first model. It provides deposit and credit products nationally across all 50 U.S. states via digital and mobile banking. However, its physical branch footprint is concentrated in key regional markets, including New York, Louisiana, Texas, Maryland, Virginia, New Jersey, and Washington D.C.

To complement its traditional branches, Capital One operates over 60 full-service "Capital One Cafés" across major U.S. metropolitan hubs like Boston, Chicago, SF, and Austin. These hybrid spaces function as community hubs, offering digital banking assistance, co-working spaces, and food/beverage discounts for cardholders.

Outside the US, Capital One maintains credit card underwriting and servicing operations in Canada and the United Kingdom. _(Capital One Financial Corp., 2025)_

#line(length: 100%)

= Market Presence

Capital One is the 6th largest US Bank Holding Company. As of December 2025, it has approximately \$600 billion in total assets and a deposit base of approximately \$480 billion. In the consumer credit card segment, Capital One is the largest card lender by total outstanding loan balances. They captured this market share by pioneering automated, digital-first account acquisition and direct-to-consumer banking via Capital One 360. This infrastructure allows the company to fund over 80% of its total loan portfolio through low-cost retail deposits and avoid the heavy funding costs associated with non-bank consumer lenders.

The strategic acquisition of Discover Financial Services fundamentally expanded Capital One's market presence. The company transitioned from a pure credit card issuer to a vertically integrated payments engine. This enables the firm to capture transaction interchange, reduce payment routing expenses, and compete directly against closed-loop networks like American Express.

At the same time, Capital One also continues to expand its premium consumer footprint through its Venture X product ecosystem and capital-light distribution channels like Capital One Cafés. This helps solidify its reach across both mass-market revolving credit and affluent consumer segments. _(Capital One Financial Corp., 2025)_

#line(length: 100%)

= Competition

Several universal commercial banks like JPMorgan Chase and Citigroup hold massive market shares in consumer lending. However, American Express (AXP) and Synchrony Financial (SYF) are the primary competitors for evaluating Capital One's financial profile.

American Express operates a closed-loop, spend-centric model tailored toward affluent consumers and corporate accounts. They derive significant top-line revenue from merchant fee volume and annual fees rather than interest charges. Conversely, Synchrony Financial specializes in a revolving-centric, private-label store card model. They acquire accounts through major merchant partnerships like Amazon and Lowe's. They generate high Net Interest Margins by lending across near-prime and subprime credit tiers. _(American Express Co., 2025) (Synchrony Financial, 2025)_

American Express & Synchrony Financial form the ideal benchmarking group for analyzing Capital One's performance because they isolate the exact structural components that form Capital One’s operational foundation. Capital One lies in the middle ground. It captures high interest yields by underwriting a broad spectrum of credit tiers, just like Synchrony Financial. However, just like American Express, it drives direct account acquisition, controls its own deposit-funding engine, and operates a proprietary payment network.

Benchmarking Capital One against American Express and Synchrony Financial would expose how different underwriting approaches, funding costs, and network capabilities influence risk-adjusted returns and net charge-off sensitivity across economic cycles.

#line(length: 100%)

= SWOT Analysis

= Strengths:

1. *Cloud-Native & Data Architecture:* The IBS engine enables real-time, precision risk-pricing.
2. *Closed-Loop Network Ownership:* Discover integration captures interchange and eliminates network rail fees paid to Visa and Mastercard.
3. *Deposit-Funded Asset Base:* Retail deposits reduce total Weighted Average Cost of Capital (WACC).

= Weaknesses:

1. *Subprime Credit Exposure:* Higher percentage of subprime borrowers elevates Net Charge-Offs (NCOs) during economic downturns compared to competitors like American Express.
2. *Capital & Regulatory Burden:* Category III bank status subjects Capital One to rigorous Federal Reserve CCAR stress testing and Category III capital requirements _(OCC, 2025) (Basel Committee on Banking Supervision, 2019)_.

= Opportunities:

1. *Debit Rail Migration:* Moving COF debit card volume onto the Discover network reduces payment routing expenses.
2. *Premium Market Expansion:* Scaling the Venture X ecosystem to challenge American Express in prime spend.

= Threats:

1. *Credit Normalization & Delinquency Spikes:* Macro headwinds hit revolving subprime balances.
2. *Regulatory Scrutiny & Interchange Limits:* Enhanced CFPB regulatory limits on late fees and merger compliance oversight.

#line(length: 100%)

#quote(block: true)[
*Note:* Financial performance metrics and balance sheet data for Capital One, American Express, and Synchrony Financial across the 2024 - 2025 period were compiled directly from their respective SEC Form 10-K filings (2024, 2025).

Daily stock price trends and equity valuation metrics were sourced via the dynamic `=GOOGLEFINANCE()` function in Google Sheets.

Financial data, ratio calculations, and stock prices are available in the accompanying spreadsheet (`BU433 Assignment Data.xlsx`).

]

#line(length: 100%)

= Stock Price Performance Analysis

Over the two-year window from January 2024 to December 2025, consumer lending institutions experienced substantial market re-valuations. Equity returns across Capital One, American Express, and Synchrony Financial were shaped by shifting Federal Reserve rate policies, credit normalization cycles, and institution-specific corporate events.

#{
  set par(justify: false)
  set text(hyphenate: true)
  table(
    columns: 4,
    [**Stock Performance Metric**],
    [**COF**],
    [**AXP**],
    [**SYF**],
    [Start Price (Jan 02, 2024)],
    [\$132.11],
    [\$188.31],
    [\$37.96],
    [End Price (Dec 31, 2024)],
    [\$178.32],
    [\$296.79],
    [\$65.00],
    [*2024 Annual Return (%)*],
    [*34.98%*],
    [*57.61%*],
    [*71.23%*],
    [End Price (Dec 31, 2025)],
    [\$242.36],
    [\$369.95],
    [\$83.43],
    [*2025 Annual Return (%)*],
    [*35.91%*],
    [*24.65%*],
    [*28.35%*],
    [*2-Year Total Return (%)*],
    [*83.45%*],
    [*96.46%*],
    [*119.78%*],
  )
}

The following chart represents the daily stock price performance of Capital One, American Express, and Synchrony Financial over the 2024-2025 timeline.

#figure(image("/Screenshot 2026-07-27 at 17.29.51.png"), caption: [])

*Key insights:*

1. Following the announcement of Capital One's \$35.5B acquisition of Discover Financial Services in February 2024, COF experienced brief stock price consolidation. Equity markets initially priced in the execution complexity and regulatory scrutiny surrounding bank merger oversight. However with time, COF's valuation steadily re-rated because of the long-term value of the acquisition.
2. During the second half of 2024, the broader financial sector benefited from Federal Reserve interest rate cuts. This led to the expansion of net interest margins across all three issuers. _(Board of Governors of the Federal Reserve System, 2024)._
3. In 2025, Capital One’s share price accelerated, outperforming both peers with a 35.91% annual gain. This was primarily because of the official regulatory approvals and the completion of the Discover integration. _(OCC, 2025)_
4. The strong correlation in price dips across all the three firms indicates that major dips were driven by industry-wide macro factors and not firm-specific operational issues.

#line(length: 100%)

= Financial Profitability & Operational Efficiency Ratios

A comparative evaluation across the 2024-2025 financial performance highlights how fundamental strategic choices influence core financial metrics. American Express leverages a fee-intensive and spend-centric model to drive superior asset returns. Synchrony Financial relies on high-yield private-label cards to maximize interest spreads. Contrary to both these firms, Capital One prioritizes balance sheet strength and sustainable spread-based revenue. The following section presents multiple metrics and ratios that helps us analyze the three firms.

= Net Interest Margin

Net Interest Margin (NIM) measures the net yield a financial institution earns on its interest-bearing assets like loans, credit card balances, and securities. A higher NIM reflects a superior loan yield price or lower funding costs.

*Company Analysis:*

1. *Capital One* maintains the lowest baseline NIM in the peer group because its asset base is diluted by lower-yielding commercial and auto loan portfolios alongside credit cards. However, they also demonstrated the strongest yield expansion, led by the stabilizing deposit costs on its direct retail platform.
2. *American Express* has a solid NIM through interest charged on revolving loan balances. The NIM slightly decreased in 2025, which reflects higher promotional interest expenses and shifting cardholder pay-in-full behaviour.
3. *Synchrony Financial* leads the sector by a wide margin. Its private-label, store-branded credit cards have a significantly higher baseline annual percentage rates (APRs). This drives the expanding, high-margin interest spreads.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/Net Interest Margin (NIM).png", width: 697pt), caption: [])

#line(length: 100%)

= Return on Assets

Return on Assets (ROA) evaluates managerial efficiency by measuring how effectively a firm generates net earnings from its asset base. A higher ROA indicates greater asset productivity and earnings power.

*Company Analysis:*

1. *Capital One*'s ROA reduced by 0.58% in 2025. This drop was primarily caused by heavy upfront loan-loss reserve builds required under CECL accounting during portfolio expansion, as well as operational integration expenses linked to the Discover Financial acquisition. _(FASB, 2016)_
2. *American Express* dominates asset efficiency across the sector. Its spend-centric model relies heavily on merchant discount fees, annual cardholder membership fees, and international service revenues. This generates a massive net-income without over-inflating total balance sheet assets.
3. *Synchrony Financial* consistently maintains high asset productivity. They benefit from a lean branchless operating footprint that minimizes total fixed assets.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/Return on Assets (ROA).png", width: 697pt), caption: [])

#line(length: 100%)

= Efficiency Ratio

The Efficiency Ratio assesses operational expense management by measuring the proportion of revenue consumed by overhead expenses. A lower efficiency ratio indicates a cost-effective operation.

*Company Analysis:*

1. *Capital One* operates within a strong range (< 60%). They highly benefit from their digital-first retail banking infrastructure. The increase in 2025 reflects temporary technology, legal, and operational expenditures required to integrate Discover's payment network.
2. *American Express* carries a high efficiency ratio because of its premium brand strategy. This stems from extensive cardholder loyalty rewards, lounge access networks, direct marketing, and customer acquisition campaigns.
3. *Synchrony Financial* has an industry-leading cost efficiency. This is mainly because its retail partners handle in-store marketing and co-brand distribution. SYF therefore can avoid major customer acquisition and physical branch expenses.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/Efficiency Ratio.png", width: 697pt), caption: [])

#line(length: 100%)

= Common Equity Tier 1 Ratio

The Common Equity Tier 1 (CET1) ratio is the fundamental regulatory metric mandated under Basel III standards to measure a bank's common equity against its risk-weighted assets. It measures a firm's ability to absorb credit shocks and macroeconomic downturns.

*Company Analysis:*

1. *Capital One* increased its CET1 ratio taking the top position among the three firms. They intentionally built this equity defense to ensure compliance with Federal Reserve CCAR stress testing, as well as to absorb potential loan markdowns and regulatory capital needs post-Discover acquisition. _(OCC, 2025)_
2. *American Express* operates with a stable CET1 ratio of 10.5%. Regulators assign lower risk weights to their asset portfolio during annual stress testing because of their affluent customer base which reduces credit default volatility. _(Basel Committee on Banking Supervision, 2019)_
3. *Synchrony Financial* reduced its CET1 ratio in 2025 as it deployed excess capital into share buybacks. They also maintained a capital buffer adequate to absorb retail card defaults.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/CET1 Ratio.png", width: 697pt), caption: [])

#line(length: 100%)

= Tier-1 Leverage Ratio

Tier 1 Leverage Ratio measures core equity capital directly against total unadjusted balance sheet assets. It acts as a non-risk-weighted safety net to prevent financial institutions from over-leveraging their balance sheets.

*Company Analysis:*

1. *Capital One* significantly strengthened its leverage position, operating at more than double the standard baseline. This confirms that Capital One's balance sheet growth is heavily backed by equity capital rather than debt issuance.
2. *American Express* maintains a consistent leverage ratio near 9.1%. This is because of their balanced equity retentions and corporate debt to fund their working capital requirements.
3. *Synchrony Financial*'s leverage ratio decreased in 2025, which is consistent with the reduction of their CET1 ratio. This confirms the active management of capital distribution while holding a comfortable buffer above the regulatory thresholds.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/Leverage Ratio.png", width: 697pt), caption: [])

#line(length: 100%)

= Risk Identification & Assessment Framework

To evaluate Capital One's resilience, let's take a look at the three core risks that they face.

= 1. Credit Risk

Capital One's primary financial threat stems from credit default risk within its revolving credit card and auto loan books. Unlike American Express, Capital One holds a significant concentration of near-prime and middle-income borrowers.

As economic conditions worsen due to inflation and rising unemployment, this group sees an earlier rise in missed payments. Moreover, CECL accounting mandates that Capital One recognize lifetime expected losses upfront upon loan origination. This creates short-term earnings volatility during growth cycles. _(FASB, 2016)_

#line(length: 100%)

= 2. Asset-Liability & Liquidity Risk

Liquidity risk arises from potential mismatches between long-duration loan assets and short-term funding liabilities.

Non-bank consumer lenders like Synchrony and American Express rely heavily on wholesale market paper, brokered CDs, and institutional debt. This leaves them vulnerable to market squeezes. Capital One mitigates this by utilizing its Capital One 360 direct branchless banking engine to capture stable, sticky retail deposits.

#line(length: 100%)

= 3. Operational & Regulatory Integration Risk

This risk arises from the execution hazards linked to the \$35.5B acquisition of Discover Financial Services.

Transitioning card portfolios onto Discover’s proprietary payment network presents technical, compliance, and cyber-operational risks. Regulators enforce heightened Category III prudential standards, requiring COF to pass rigorous Federal Reserve CCAR stress tests. _(OCC, 2025) (Basel Committee on Banking Supervision, 2019)_

#line(length: 100%)

= Risk Evaluation

Capital One actively manages these identified exposures using three strategic controls:

1. *Machine Learning & Dynamic Pricing:* Capital One uses proprietary automated algorithms to continually assess borrower health and to dynamically adjust credit limits before any charge-offs.
2. *Deposit-Funded Balance Sheet Architecture:* Capital One insulates its funding model from wholesale credit market freezes and interest rate shocks by maintaining an extensive retail deposit base.
3. *Capital Buffer:* Capital One maintains core capital buffers well above regulatory baselines. This allows them to absorb stress-test scenarios, credit shocks, and Discover integration friction without threatening systemic solvency.

#line(length: 100%)

= Quantitative Risk Management Metrics

= Net Charge-Off Rate

The Net Charge-Off (NCO) rate is the definitive measure of credit default risk and portfolio quality. It represents the percentage of total loans unlikely to be recovered after all collection efforts have been exhausted. A lower NCO indicates tighter underwriting standards and higher borrower creditworthiness.

*Company Analysis:*

1. *Capital One* occupies a balanced risk position. The NCO rate improved in 2025, which demonstrates stronger risk management controls.
2. *American Express* maintains the industry's lowest NCO rate. Its strict focus on high-net-worth prime borrowers creates an insulated credit profile with minimal default exposure.
3. *Synchrony Financial* bears the highest credit risk in the group. Operating in private-label retail store cards, SYF accepts substantial default rates as a cost of doing business.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/NCO Rate.png", width: 697pt), caption: [])

#line(length: 100%)

= Loan-to-Deposit Ratio

The Loan-to-Deposit Ratio evaluates Asset-Liability Management and liquidity risk by measuring the extent to which a firm's loan portfolio is funded by stable, insured customer deposits versus capital market borrowings. An LTD ratio below 100% indicates that every dollar of loans is fully backed by deposits, shielding the institution from market liquidity shocks.

*Company Analysis:*

1. *Capital One* maintains the most resilient liquidity profile in the peer group as the only firm with an LTD ratio below 100%. The entire loan portfolio is funded through \$475B+ in customer deposits captured via the direct Capital One 360 platform. This completely eliminates reliance on volatile wholesale debt markets for core loan funding.
2. *American Express* operates at the highest LTD ratio in the group, which reflects a structural imbalance between its rapidly growing credit card loan portfolio and its smaller deposit base. However, the LTD ratio decreased in 2025 as management actively expanded its high-yield consumer deposit product to diversify its funding mix.
3. *Synchrony Financial* maintains a high LTD ratio between Capital One and American Express. They rely heavily on high-yield online savings accounts and brokered deposits to fund their private-label store cards. The ratio remained essentially flat in 2025 because deposit growth roughly matched loan expansion. Because the ratio is more than 100%, Synchrony Financial must consistently access secondary wholesale debt markets to cover its excess lending balance.

#figure(image("/Uni/Spring 2026/BU433/BU433 Assignment/Charts/LTD Ratio.png", width: 697pt), caption: [])

#line(length: 100%)

= Short-Term Performance Forecasts

The following section discusses Capital One's operational and financial short-term performance. The acquisition of Discover Financial Services will play a major role in Capital One's near-term future.

1. *Vertical Integration & Fee Synergy* Capital One has begun transitioning its debit card volumes and select credit card portfolios onto the Discover payment network. This shift off third-party processors will eliminate substantial external payment rail fees paid to the third parties. _(Capital One Financial Corp., 2024)_
  The Discover Financial transition will also circumvent traditional interchange rate caps imposed on large covered banks. This will enable Capital One to directly capture higher merchant discount transaction revenues. _(Capital One Financial Corp., 2024)_

  The transition is projected to yield approximately \$1.2B in annual run-rate network synergies and \$1.5B in annualized cost reductions as account migration finishes. _(Capital One Financial Corp., 2024)_

2. *Efficiency Ratio & Cost Structure* Operating expenses will continue to remain elevated through late 2026 due to platform migration expenditures, technology consolidation, legal compliance, and account integration friction. Hence, the Efficiency Ratio will continue to be around 56% - 58%.
  However, as the duplicate cloud environments are phased out and customer servicing is unified under Capital One's digital platform, operating leverage will accelerate and drive the efficiency ratio downward to around 52%.

3. *Return on Assets & Earning Power* Capital One’s Return on Assets fell to 0.41% in 2025 due to heavy upfront CECL credit loss provisioning and merger integration costs. As upfront reserve additions normalize and synergy realization accelerates, ROA is forecasted to rebound toward historical benchmark targets of 1.00% - 1.15%. _(FASB, 2016)_
4. *Solvency, Capital Structure & Credit Quality* Capital One's current CET1 ratio is around 14.27%. As the merger integration risks decrease, the management is expected to redeploy excess capital buffer through share repurchases and dividend increases. This will guide the CET1 ratio toward the target operating range of 12% - 12.5%.
  Net Charge-Offs are also expected to stabilize around 3% - 3.3%. Capital One’s real-time machine learning underwriting engines allow management to dynamically adjust credit lines before any credit defaults. This limits their downside credit losses while expanding prime product offerings. _(Capital One Financial Corp., 2025)_


To summarize, Capital One's financial trajectory over the near-term strategic horizon is defined by the integration of Discover Financial Services. This brings some short-term operational friction like heavy upfront technological integration costs and legal reserves. However in the long-term, it will lead to massive efficiencies and cost optimizations, allowing Capital One to transition into being a fully vertically integrated network owner. This positions the company to drive sustained EPS expansion and long-term shareholder value across economic cycles.

#line(length: 100%)

= References

1. *American Express Company.* (2025). _Form 10-K: Annual Report for the fiscal year ended December 31, 2024_. U.S. Securities and Exchange Commission.
2. *American Express Company.* (2026). _Form 10-K: Annual Report for the fiscal year ended December 31, 2025_. U.S. Securities and Exchange Commission.
3. *Basel Committee on Banking Supervision.* (2019). _Basel III: Finalising post-crisis reforms_. Bank for International Settlements (BIS).
4. *Board of Governors of the Federal Reserve System.* (2024). _Dodd-Frank Act Stress Test 2024: Supervisory Stress Test Results_. Federal Reserve System Publications.
5. *Board of Governors of the Federal Reserve System.* (2025). _Order Approving the Acquisition of a Bank Holding Company: Capital One Financial Corporation / Discover Financial Services_. Federal Reserve Press Releases.
6. *Capital One Financial Corp.* (2024, February 20). _Capital One to acquire Discover: Investor presentation_. Capital One Investor Relations.
7. *Capital One Financial Corporation.* (2025). _Form 10-K: Annual Report for the fiscal year ended December 31, 2024_. U.S. Securities and Exchange Commission.
8. *Capital One Financial Corporation.* (2026). _Form 10-K: Annual Report for the fiscal year ended December 31, 2025_. U.S. Securities and Exchange Commission.
9. *Clemons, E. K., & Thatcher, M. E.* (1998). _Capital One: Exploiting an Information-Based Strategy_. Wharton School, University of Pennsylvania.
10. *Financial Accounting Standards Board (FASB).* (2016). _Accounting Standards Update No. 2016-13: Financial Instruments - Credit Losses (Topic 326): Measurement of Credit Losses on Financial Instruments (CECL)_.
11. *Office of the Comptroller of the Currency (OCC).* (2025). _Conditional Approval of Capital One, National Association to Acquire Discover Bank_ (News Release 2025-36).
12. *Synchrony Financial.* (2025). _Form 10-K: Annual Report for the fiscal year ended December 31, 2024_. U.S. Securities and Exchange Commission.
13. *Synchrony Financial.* (2026). _Form 10-K: Annual Report for the fiscal year ended December 31, 2025_. U.S. Securities and Exchange Commission.

#line(length: 100%)

