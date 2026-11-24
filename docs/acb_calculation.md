# ACB Calculation by CRA Definition

Source: [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/special-rules-other-transactions.html)

Properties of a group are considered to be identical if each property in the group is the same as all the others. The most common examples of identical properties are shares of the same class of the capital stock of a corporation or units of a mutual fund trust.

You may buy and sell several identical properties at different prices over a period of time. If you do this, you have to calculate the average cost of each property in the group at the time of each purchase to determine your adjusted cost base (ACB) . Dispositions of identical properties do not affect the ACB.

The average cost is calculated by dividing the total cost of identical properties purchased (this is usually the cost of the property plus any expenses involved in acquiring it) by the total number of identical properties owned.

Generally, the following properties are not considered identical properties:

- securities acquired under an employee option agreement that are subject to the benefit deferral or are designated and disposed of within 30 days
- certain employer shares received by an employee as part of a lump-sum payment upon withdrawal from a deferred profit sharing plan

**Example 1**

Over the years, you have bought and sold common shares of STU Ltd. This example shows how, after each purchase, the ACB of your shares changes.

In 2001, you purchased 100 shares for $1,500. The ACB is therefore $15.00 ($1,500 ÷ 100).

In 2006, you purchased an additional 150 shares for $3,000. The new ACB is calculated by dividing the total cost of the shares of STU Ltd. ($1,500 + $3,000 = $4,500) by the total number of shares you have purchased (100 + 150 = 250). Therefore, the ACB is $18.00 ($4,500 ÷ 250).

In 2008, you sold 200 shares for $3,600. The ACB remains at $18.00 per share.

In 2025, you purchased 350 shares for $7,350. The new ACB is $20.63 [($900 + $7,350) ÷ (50 + 350)].

## Calculation (example)

- t=0: take the average cost of all purchased shares
- purchase event: `new_cost_base = (cost_of_owned_shares + cost_of_purchased_shares) / total_shares_purchased`
- sell event: cost base doesn't change, `total_shares_purchased = total_shares_purchased - shares_sold`
- purchase after sell: `new_cost_base = (cost_of_remaining_owned_shares + cost_of_purchased_shares) / total_shares_purchased`
