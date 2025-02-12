import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class DiscountedCashflow(Base):
    @requires_plan(FMPPlan.BASIC)
    async def aDCF_valuation(self, symbol: str) -> list[dict]:
        '''
        Estimate the intrinsic value of a company. 
        Calculate the DCF valuation based on expected future cash flows and discount rates.
        '''
        endpoint = 'discounted-cash-flow'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def DCF_valuation(self, symbol: str) -> list[dict]:
        return asyncio.run(self.aDCF_valuation(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def alevered_DCF(self, symbol: str, limit: int | None = None) -> list[dict]:
        '''
        Analyze a company’s value, which incorporates the impact of debt. 
        This provides post-debt company valuation, offering investors a more accurate measure of a company's true worth by accounting for its debt obligations.
        '''
        endpoint = 'levered-discounted-cash-flow'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def levered_DCF(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.alevered_DCF(symbol, limit))
    
    @requires_plan(FMPPlan.STARTER)
    async def acustom_DCF_advanced(
        self,
        symbol: str,
        revenueGrowthPct: float | None = None,
        ebitdaPct: float | None = None,
        depreciationAndAmortizationPct: float | None = None,
        cashAndShortTermInvestmentsPct: float | None = None,
        receivablesPct: float | None = None,
        inventoriesPct: float | None = None,
        payablePct: float | None = None,
        ebitPct: float | None = None,
        capitalExpenditurePct: float | None = None,
        operatingCashFlowPct: float | None = None,
        sellingGeneralAndAdministrativeExpensesPct: float | None = None,
        taxRate: float | None = None,
        longTermGrowthRate: float | None = None,
        costOfDebt: float | None = None,
        costOfEquity: float | None = None,
        marketRiskPremium: float | None = None,
        beta: float | None = None,
        riskFreeRate: float | None = None,
    ) -> list[dict]:
        '''
        Run a tailored Discounted Cash Flow (DCF) analysis. 
        This allows users to fine-tune their assumptions and variables, offering a more personalized and precise valuation for a company.
        '''
        endpoint = 'custom-discounted-cash-flow'
        params = {'symbol': symbol}
        if revenueGrowthPct:
            params['revenueGrowthPct'] = revenueGrowthPct
        if ebitdaPct:
            params['ebitdaPct'] = ebitdaPct
        if depreciationAndAmortizationPct:
            params['depreciationAndAmortizationPct'] = depreciationAndAmortizationPct
        if cashAndShortTermInvestmentsPct:
            params['cashAndShortTermInvestmentsPct'] = cashAndShortTermInvestmentsPct
        if receivablesPct:
            params['receivablesPct'] = receivablesPct
        if inventoriesPct:
            params['inventoriesPct'] = inventoriesPct            
        if payablePct:
            params['payablePct'] = payablePct
        if ebitPct:
            params['ebitPct'] = ebitPct
        if capitalExpenditurePct:
            params['capitalExpenditurePct'] = capitalExpenditurePct
        if operatingCashFlowPct:
            params['operatingCashFlowPct'] = operatingCashFlowPct
        if sellingGeneralAndAdministrativeExpensesPct:
            params['sellingGeneralAndAdministrativeExpensesPct'] = sellingGeneralAndAdministrativeExpensesPct
        if taxRate:
            params['taxRate'] = taxRate
        if longTermGrowthRate:
            params['longTermGrowthRate'] = longTermGrowthRate
        if costOfDebt:
            params['costOfDebt'] = costOfDebt
        if costOfEquity:
            params['costOfEquity'] = costOfEquity
        if marketRiskPremium:
            params['marketRiskPremium'] = marketRiskPremium
        if beta:
            params['beta'] = beta
        if riskFreeRate:
            params['riskFreeRate'] = riskFreeRate
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def custom_DCF_advanced(
        self,
        symbol: str,
        revenueGrowthPct: float | None = None,
        ebitdaPct: float | None = None,
        depreciationAndAmortizationPct: float | None = None,
        cashAndShortTermInvestmentsPct: float | None = None,
        receivablesPct: float | None = None,
        inventoriesPct: float | None = None,
        payablePct: float | None = None,
        ebitPct: float | None = None,
        capitalExpenditurePct: float | None = None,
        operatingCashFlowPct: float | None = None,
        sellingGeneralAndAdministrativeExpensesPct: float | None = None,
        taxRate: float | None = None,
        longTermGrowthRate: float | None = None,
        costOfDebt: float | None = None,
        costOfEquity: float | None = None,
        marketRiskPremium: float | None = None,
        beta: float | None = None,
        riskFreeRate: float | None = None,
    ) -> list[dict]:
        return asyncio.run(self.acustom_DCF_advanced(
            symbol, revenueGrowthPct, ebitdaPct, depreciationAndAmortizationPct, cashAndShortTermInvestmentsPct, receivablesPct, inventoriesPct, payablePct, ebitPct, capitalExpenditurePct, operatingCashFlowPct, sellingGeneralAndAdministrativeExpensesPct, taxRate, longTermGrowthRate, costOfDebt, costOfEquity, marketRiskPremium, beta, riskFreeRate
        ))
    
    @requires_plan(FMPPlan.STARTER)
    async def acustom_DCF_levered(
        self,
        symbol: str,
        revenueGrowthPct: float | None = None,
        ebitdaPct: float | None = None,
        depreciationAndAmortizationPct: float | None = None,
        cashAndShortTermInvestmentsPct: float | None = None,
        receivablesPct: float | None = None,
        inventoriesPct: float | None = None,
        payablePct: float | None = None,
        ebitPct: float | None = None,
        capitalExpenditurePct: float | None = None,
        operatingCashFlowPct: float | None = None,
        sellingGeneralAndAdministrativeExpensesPct: float | None = None,
        taxRate: float | None = None,
        longTermGrowthRate: float | None = None,
        costOfDebt: float | None = None,
        costOfEquity: float | None = None,
        marketRiskPremium: float | None = None,
        beta: float | None = None,
        riskFreeRate: float | None = None,
    ) -> list[dict]:
        '''
        Run a tailored Discounted Cash Flow (DCF) analysis. 
        This allows users to fine-tune their assumptions and variables, offering a more personalized and precise valuation for a company.
        '''
        endpoint = 'custom-levered-discounted-cash-flow'
        params = {'symbol': symbol}
        if revenueGrowthPct:
            params['revenueGrowthPct'] = revenueGrowthPct
        if ebitdaPct:
            params['ebitdaPct'] = ebitdaPct
        if depreciationAndAmortizationPct:
            params['depreciationAndAmortizationPct'] = depreciationAndAmortizationPct
        if cashAndShortTermInvestmentsPct:
            params['cashAndShortTermInvestmentsPct'] = cashAndShortTermInvestmentsPct
        if receivablesPct:
            params['receivablesPct'] = receivablesPct
        if inventoriesPct:
            params['inventoriesPct'] = inventoriesPct            
        if payablePct:
            params['payablePct'] = payablePct
        if ebitPct:
            params['ebitPct'] = ebitPct
        if capitalExpenditurePct:
            params['capitalExpenditurePct'] = capitalExpenditurePct
        if operatingCashFlowPct:
            params['operatingCashFlowPct'] = operatingCashFlowPct
        if sellingGeneralAndAdministrativeExpensesPct:
            params['sellingGeneralAndAdministrativeExpensesPct'] = sellingGeneralAndAdministrativeExpensesPct
        if taxRate:
            params['taxRate'] = taxRate
        if longTermGrowthRate:
            params['longTermGrowthRate'] = longTermGrowthRate
        if costOfDebt:
            params['costOfDebt'] = costOfDebt
        if costOfEquity:
            params['costOfEquity'] = costOfEquity
        if marketRiskPremium:
            params['marketRiskPremium'] = marketRiskPremium
        if beta:
            params['beta'] = beta
        if riskFreeRate:
            params['riskFreeRate'] = riskFreeRate
        return await self._request(endpoint, params=params)        
    
    @requires_plan(FMPPlan.STARTER)
    def custom_DCF_levered(
        self,
        symbol: str,
        revenueGrowthPct: float | None = None,
        ebitdaPct: float | None = None,
        depreciationAndAmortizationPct: float | None = None,
        cashAndShortTermInvestmentsPct: float | None = None,
        receivablesPct: float | None = None,
        inventoriesPct: float | None = None,
        payablePct: float | None = None,
        ebitPct: float | None = None,
        capitalExpenditurePct: float | None = None,
        operatingCashFlowPct: float | None = None,
        sellingGeneralAndAdministrativeExpensesPct: float | None = None,
        taxRate: float | None = None,
        longTermGrowthRate: float | None = None,
        costOfDebt: float | None = None,
        costOfEquity: float | None = None,
        marketRiskPremium: float | None = None,
        beta: float | None = None,
        riskFreeRate: float | None = None,
    ) -> list[dict]:
        return asyncio.run(self.acustom_DCF_levered(
            symbol, revenueGrowthPct, ebitdaPct, depreciationAndAmortizationPct, cashAndShortTermInvestmentsPct, receivablesPct, inventoriesPct, payablePct, ebitPct, capitalExpenditurePct, operatingCashFlowPct, sellingGeneralAndAdministrativeExpensesPct, taxRate, longTermGrowthRate, costOfDebt, costOfEquity, marketRiskPremium, beta, riskFreeRate
        ))
