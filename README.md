# ACB Calculator

## User Stories

- upload investment statements
- validate and deduplicate entries
- check ACB data for completeness
    - configurable expected statements (quarterly default)
- calculate adjusted cost basis (ACB) for Canadian tax purposes for a given tax year
    - lookup historical USD -> CAD exchange rate from Bank of Canada for calculating ACB
- store past statements in a database for auditing/tracking/calculating
- output calculated ACB for entry into tax forms

## Architecture

- Python
- Flask
- PostgreSQL
- Docker
