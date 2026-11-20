# Portfolio risk: the maths

## 1. Notation

| Symbol | Meaning |
|---|---|
| $X$ | A random variable |
| $\sigma_X$ | Standard deviation (volatility) of X |
| $\mu_X$ | The mean (average) **return** of X over n days |
| E [ . ] | The average over data inside bracket |
| $\sigma^2 _X$ or Var(X) | Variance: average squared distance from mean |
| Cov(X,Y) or $\sigma_{XY}$ | Covariance of X and Y |
| $\rho_{XY}$ | Correlation of X and Y, covariant rescale between [-1, 1] |
| $w_i$ | Weight of item index i |
| w | All weights togheter, stack values, a vector |
| $w^\top$ | w transposed: the same weights written as a row instead of a column |
| $\Sigma$ | Covariance Matrix, not to confuse with Summation |


## 2. Mean, variance and standard deviation

**Mean**: The ordinary average over the long run E[X]

$$\mu_X = \frac{1}{n}\sum_{t=1}^{n} x_t$$

**Deviation**: How far the day's return is from the mean

$$deviation\ of\ the\ day\ t = x_t - \mu_X $$

**Variance**: The average squared of all the deviations

$$
\sigma_X^2 = \operatorname{Var}(X) = E\big[(X - \mu_X)^2\big] \approx \frac{1}{n}\sum_{t=1}^{n} (x_t - \mu_X)^2
$$

Variance looks only at one asset.

**Standard Deviation**: Also known as volatility

$$
\sigma_X = \sqrt{\sigma_X^2}
$$


## 3. Covariance and correlation

We also need to know if the movement of two assets go and down at the same time.

**Covariance**: Average of the sync/unsyncronized movmeent of the two assets.

$$
\operatorname{Cov}(X,Y) = E\big[(X - \mu_X)(Y - \mu_Y)\big] \approx \frac{1}{n}\sum_{t=1}^{n} (x_t - \mu_X)(y_t - \mu_Y)
$$

Both above their mean $(+x+) or (-x-)$ = Positive *Move togheter*

One above and one bellow their mean (+x-) or (-x+) = Negative *Move opposite*

**Correlation**: Covariance on a scale of [-1, 1]

Covariance is in %² and grows with how volatile the assets are. Dividing by both standard deviations removes the units.

$$
\rho_{XY} = \frac{\operatorname{Cov}(X,Y)}{\sigma_X \, \sigma_Y}, \qquad -1 \le \rho_{XY} \le 1
$$

Rearranging the terms gives:

$$
\operatorname{Cov}(X,Y) = \rho_{XY} \, \sigma_X \, \sigma_Y
$$


## 4. Weights and portfolio return

**Weight**: $w_i$ of asset i is the fraction of the contribution out of the total pool


**Portfolio Return**: The sum of all weighted contributions. **Only used on simple returns, log returns dont add up across assets this way**

$$
R_p = w_1 X + w_2 Y = \sum_i w_i R_i = w^\top R
$$


## 5. Portfolio variance (Derivation)

The risk of the the portfolio, the variance of the portfolio return.


Portfolio return: $R_p = w_1 X + w_2 Y$.

**Step 1: the mean.** Expectation is linear, so

$$
E[R_p] = w_1\mu_X + w_2\mu_Y
$$

**Step 2: the deviation from the mean.**

$$
R_p - E[R_p] = w_1(X - \mu_X) + w_2(Y - \mu_Y)
$$

**Step 3: square it,** using $(A+B)^2 = A^2 + 2AB + B^2$:

$$
\big(R_p - E[R_p]\big)^2 = w_1^2 (X-\mu_X)^2 \;+\; \ 2w_1w_2(X-\mu_X)(Y-\mu_Y) \;+\; w_2^2 (Y-\mu_Y)^2
$$

**Step 4: take the expectation of each term.** The weights are constants, so they come out of $E$:

$$
\sigma_p^2 = E\Big[\big(R_p - E[R_p]\big)^2\Big]
= w_1^2\, E\big[(X-\mu_X)^2\big] + 2w_1w_2\, E\big[(X-\mu_X)(Y-\mu_Y)\big] + w_2^2\, E\big[(Y-\mu_Y)^2\big]
$$

**Step 5: recognise the definitions** from sections 2 and 3:

$$
\sigma_p^2 = w_1^2\,Var(X) \;+\; w_2^2\,Var(Y)\;+\; 2\,w_1 w_2\,Cov(X,Y)
$$



$$
\sigma_p^2 = w_1^2\,\sigma_X^2 \;+\; w_2^2\,\sigma_Y^2 \;+\; 2\,w_1 w_2\,\operatorname{Cov}(X,Y)
$$

- $w_1^2\sigma_X^2$: Ex: SPY's own risk, scaled by how much of it you hold.
- $w_2^2\sigma_Y^2$: the same for TLT.
- $2w_1w_2\operatorname{Cov}(X,Y)$: the **interaction term**. If the covariance is negative, this term is negative and reduces total risk.

**Matrix form**

With 4 assets (SPY, QQQ, TLT, GLD) the formula above would have 4 squared terms and 6 cross terms. Matrices write it compactly.

**Covariance matrix** $\Sigma$: row $i$, column $j$ holds $\operatorname{Cov}(\text{asset } i, \text{asset } j)$.

$$
\Sigma = \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{21} & \sigma_2^2 \end{pmatrix}
$$

- On the diagonal ($i = j$) each entry is that asset's variance, because $\operatorname{Cov}(X,X) = \operatorname{Var}(X)$.
- Here $\sigma_{12}$ is shorthand for $\operatorname{Cov}(X,Y)$.
- $\Sigma$ is symmetric ($\sigma_{21} = \sigma_{12}$) because $\operatorname{Cov}(X,Y) = \operatorname{Cov}(Y,X)$.

Example:

$$
\Sigma = \begin{pmatrix} 4.4 & -2.6 \\ -2.6 & 2 \end{pmatrix}
$$

Thus, 

$$
\sigma_p^2 = w^\top \Sigma\, w
$$

The portfolio variance $\sigma_p^2$ by itself doesnt tell much with %$^2$ as the result of much much the portfolio moves squared. However, the Volatility: $\sigma_p$ can tell us on average how much the portfolio moves per day $\pm\sigma_p$.


## 6. Diversification

Lower portfolio variance, lower the risk but do **not imply** more optimized diversification.

Where 1.645 comes from?

If daily returns follow a normal (bell-curve) distribution with mean ≈ 0 and standard deviation $\sigma_p$, then a return below $-1.645\,\sigma_p$ happens on only 5% of days. (1.645 is the 95th percentile of the standard normal distribution). So the 95% one-day VaR in dollars is:

$$ \text{VaR}_{95\%} = 1.645 \times \sigma_p \times V $$

This is the lost threshold on about 5% of the days if the return distribution follows a gaussian distribution.

Let $ V = 1,000,000\$,\ \sigma_p = 0.695\%$

$ \text{VaR}_{95\%} = 1.645 \times \sigma_p \times V = 11,430$ $

On 95% of days the portfolio should lose less than 11,430 USD.
On the worst 5% of days (about 12–13 days a year), the loss exceeds 11,430 USD.
VaR does not say how much bigger those losses are. CVaR answers that.

