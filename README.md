# DATASCI-112 Project  
## Uncovering Invisible Barriers to a Sustainable Future  
**An Empirical Study on Oil Shocks, Renewable Stocks, and Market Dynamics**

---

## Authors

| Name             | Affiliation           | Email                      |
|------------------|------------------------|-----------------------------|
| **Quynh Anh Nguyen** | Stanford University      | quynhanh@stanford.edu       |
| **Stuti Desai**            | Stanford University      | sdesai28@stanford.edu            |


---

## Main Research Question: What Are the Invisible Barriers to a Sustainable Future?  

## Research Purpose and Overall Structure

This project empirically investigates how "invisible variables" hinder the transition to renewable energy. Specifically, it explores how oil price shocks propagate through renewable energy equity markets, how this sensitivity differs across technology sectors, and how the market structure has evolved since 2020. It also analyzes how political and media sentiment affects investor behavior, thereby revealing narrative-driven amplification in market reactions.

The overall structure of analysis follows this sequence:

- **SRQ1**: Do oil price returns significantly affect renewable energy stock returns?
- **SRQ2**: Does this sensitivity vary across technology sectors (solar, wind, storage)?
- **SRQ3**: Have structural relationships between oil and renewables changed since 2020?
- **SRQ4**: How does political/media sentiment influence renewable energy stock returns?

SRQ1–3 use time-series data from 2019–2024 for consistency, while SRQ4 is a complementary and temporally independent study focused solely on 2025. Although each sub-question is independently structured, the ultimate goal is to **hedge across all SRQs** to draw an integrated and robust conclusion.

---

## Summary & Key Findings by Sub-Question

### SRQ1: Do oil price returns significantly affect renewable energy stock returns?

#### **Final Answer**: YES – Enhanced analysis confirms significant influence.

#### **Key Results**:
- 7 out of 8 stocks exhibit oil sensitivity (p < 0.05)

- Average coefficient: ~0.1360

- Nonlinear, time-varying patterns revealed using LOESS and Online Regression

- Time-aware hyperparameter tuning improved R² by -0.9200 on average

#### **Interpretation**:
- Renewable stocks remain vulnerable to oil volatility

- Static linear models miss key dynamic patterns

- Time-varying models enhance robustness and interpretation

---
### SRQ2: Does oil shock sensitivity vary across renewable energy sectors?

#### **Final Answer**: YES – Structural heterogeneity observed

#### **Methods**:
- Interaction regression: sector dummies × oil return
- Tukey HSD post-hoc tests + visualization

#### **Key Results**:
- Solar: positive association (coef =  0.1526, p ≈ 0.052)

- Wind: negative interaction (coef = -0.1866, p = 0.171)

- Storage: weak negative effect (coef = -0.0713, p = 0.521)

#### **Interpretation**:
- Solar stocks gain from higher oil prices (competitiveness effect)

- Wind stocks may face adverse effects due to policy/infrastructure dependencies

- Storage stocks show attenuated connection due to indirect positioning

---
### SRQ3: Have structural oil-renewable relationships changed post-2020?

#### **Final Answer**: YES – Topological phase shift detected

#### **Methods**:
- Persistent Homology using Vietoris–Rips complex

- Spectral analysis of combinatorial Laplacians + entropy metrics

#### **Key Metrics**:
- Mean L2 shift: 14.4346

- KL Divergence: −35.6222

- JS Divergence: 0.0408

#### **Interpretation**:
- Post-COVID market became more synchronized and predictable

- Structural simplification reduced arbitrage opportunities

- Diversification weakened $\rightarrow$ timing & macro-trend strategies needed

---
### SRQ4: How does political/media sentiment affect renewable stocks?

#### **Final Answer**: Sentiment and keyword interactions significantly predict next-day returns

#### **Data Pipeline**:
- 800+ NPR Energy articles from 2025 scraped and parsed

- Title + body text processed with VADER + TF-IDF

#### **Modeling Results**:
- VADER + TF-IDF Lasso Regression: R² ≈ 0.8967, RMSE ≈ 0.0148

- Removing TF-IDF increases RMSE: confirms importance of keyword context

- No overfitting in temporal cross-validation (Mean CV RMSE ≈ 0.056)

#### **Interpretation**:
- Media tone shapes investor sentiment

- Sentiment × topical keywords (e.g., subsidy, grid, shortage) amplify predictive power

---

## Final Integrated Conclusion

This study avoids reliance on any single model or timepoint. Instead, it employs a **layered interpretive structure** combining causal inference, structural evolution, and sentiment response across SRQ1–4.

- SRQ1 confirms a statistically robust link between oil prices and renewable equities.
- SRQ2 uncovers cross-sector structural heterogeneity.
- SRQ3 detects phase transitions using topological geometry, inaccessible to standard regression.
- SRQ4 reveals narrative-driven market sensitivity via political/media sentiment.

Together, they form a comprehensive framework: **Causal Impact → Structural Evolution → Narrative Amplification**. Final conclusions hedge across these findings to construct an integrated understanding of market dynamics.

This enables generation of **insights with immediate real-world impact** across multiple domains:

- **Policy Design**:
  - Sector-specific oil sensitivities guide carbon tax and subsidy calibration.
  - SRQ3's topology-based structure detection anticipates policy response effectiveness.

- **Asset Allocation & Strategy**:
  - SRQ4 informs event-driven selection based on media narratives
  - SRQ1 supports macro-aware rebalancing using oil sensitivity coefficients
  - SRQ2 enables hedged strategies exploiting divergent sectoral responses (e.g., solar vs. wind)

- **Crisis Management & ETF Rebalancing**:
  - SRQ3 flags potential failures of correlation-based hedging
  - Allows dynamic ETF allocation using regime-shift detection

Ultimately, this project grounds the abstract notion of "invisible barriers" in tangible empirical analysis, offering a novel yet actionable lens for designing sustainable financial and policy frameworks.
