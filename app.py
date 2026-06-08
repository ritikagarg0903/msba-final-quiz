import streamlit as st
import random

st.set_page_config(
    page_title="MSBA 2026 Exam Practice",
    page_icon="🎓",
    layout="centered",
)

st.markdown("""
<style>
/* Radio button option labels */
div[data-testid="stRadio"] label p {
    font-size: 1.1rem !important;
}
/* Checkbox option labels */
div[data-testid="stCheckbox"] label p {
    font-size: 1.1rem !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# QUESTION BANK
# ─────────────────────────────────────────────
QUESTIONS = [
    # ── ANALYTIC DECISION MAKING ──────────────
    {
        "section": "Analytic Decision Making",
        "question": "Linear programming cannot be used to solve dynamic problems.",
        "type": "tf",
        "answer": "False",
        "reasoning": "LP can be adapted to handle multi-period (dynamic) problems by formulating each time period as a stage in a multi-period linear program. The claim that it *cannot* be used is too absolute and therefore false.",
    },
    {
        "section": "Analytic Decision Making",
        "question": "In linear programming, constraints always define a convex set.",
        "type": "tf",
        "answer": "False",
        "reasoning": "While a standard LP feasible region formed by linear inequalities is convex, the presence of integer constraints or conflicting constraints (infeasible region) can produce a non-convex or empty feasible set. The word 'always' makes this false.",
    },
    {
        "section": "Analytic Decision Making",
        "question": "A maximization problem can always be defined as a minimization problem by multiplying each constraint by -1.",
        "type": "tf",
        "answer": "False",
        "reasoning": "To convert a maximization to minimization, you negate the **objective function** (multiply by −1), not the constraints. Multiplying constraints by −1 only flips their inequality direction (≤ becomes ≥) but does not change the problem type.",
    },
    {
        "section": "Analytic Decision Making",
        "question": "Which of the following is NOT a typical assumption of linear programming models?",
        "type": "mcq",
        "options": {"A": "Proportionality", "B": "Additivity", "C": "Certainty", "D": "Nonlinearity"},
        "answer": "D",
        "reasoning": "LP assumes Proportionality (objective and constraints scale linearly with variables), Additivity (contributions of variables add up independently), and Certainty (all parameters are known constants). Nonlinearity is the *opposite* of what LP requires — LP is by definition a linear model.",
    },
    {
        "section": "Analytic Decision Making",
        "question": "A convex feasible region implies that:",
        "type": "mcq",
        "options": {
            "A": "Every local maximum is also a global maximum",
            "B": "There may be no optimal solution",
            "C": "There is only one feasible solution",
            "D": "All decision variables must be binary",
        },
        "answer": "A",
        "reasoning": "A key property of convex optimization: any local optimum in a convex feasible region is also a global optimum. There are no 'local traps.' This is why LP — which always has a convex feasible region — can be solved efficiently to guaranteed global optimality.",
    },
    {
        "section": "Analytic Decision Making",
        "question": "Integer programming is most critical when:",
        "type": "mcq",
        "options": {
            "A": "All decisions can be fractional",
            "B": "Decisions are discrete, like yes/no selections",
            "C": "There is uncertainty in data",
            "D": "The feasible region is non-convex",
        },
        "answer": "B",
        "reasoning": "Integer programming is needed when decision variables must take whole-number (or binary) values — such as whether to open a facility (0 or 1), how many trucks to deploy, etc. Fractional solutions like '2.7 trucks' are physically meaningless in such contexts.",
    },
    {
        "section": "Analytic Decision Making",
        "question": "Selling diapers vs. selling fast fashion: In the case of diapers, firms should apply revenue management (a form of markdown pricing).",
        "type": "tf",
        "answer": "False",
        "reasoning": "Revenue management and markdown pricing are suited for products with perishable or time-sensitive value — like airline seats or fashion items that go out of style. Diapers are a staple commodity with consistent, ongoing demand and no expiry pressure, so markdown pricing strategies do not apply.",
    },
    # ── BIG DATA ─────────────────────────────
    {
        "section": "Big Data",
        "question": "You are designing a feature-computation layer that must route every user's events to the same downstream worker so that stateful aggregation remains consistent. Which mechanism best achieves this guarantee?",
        "type": "mcq",
        "options": {
            "A": "Round-robin load balancing",
            "B": "Consistent hashing",
            "C": "Random partitioning with a shared database",
            "D": "Reservoir sampling",
        },
        "answer": "B",
        "reasoning": "Consistent hashing maps each user ID deterministically to the same worker node. Unlike round-robin (which distributes without stickiness) or random partitioning (which loses state locality), consistent hashing guarantees that all events for a given user always land on the same worker, enabling stateful aggregation without cross-worker coordination.",
    },
    {
        "section": "Big Data",
        "question": "A Bloom filter returns 'possibly in set' for an element. Which of the following is the most accurate interpretation of this result?",
        "type": "mcq",
        "options": {
            "A": "The element is definitely in the set",
            "B": "The element is definitely not in the set",
            "C": "The element may or may not be in the set; false positives are possible",
            "D": "The filter must be rebuilt before any further queries",
        },
        "answer": "C",
        "reasoning": "A Bloom filter has two possible responses: 'definitely NOT in set' (no false negatives) or 'possibly in set' (may be a false positive due to hash collisions). When it says 'possibly in set,' the element may or may not actually be present — you get a guaranteed 'no' but only a probabilistic 'yes.'",
    },
    {
        "section": "Big Data",
        "question": "In Kafka, a consumer group has 4 consumers and a topic has 6 partitions. What is the most likely partition assignment?",
        "type": "mcq",
        "options": {
            "A": "Each consumer reads 1.5 partitions on average; partial reads are possible",
            "B": "Two consumers each read 2 partitions; two consumers each read 1; all partitions are covered",
            "C": "All 4 consumers read all 6 partitions in parallel",
            "D": "Only 4 partitions will be consumed; the other 2 will be skipped",
        },
        "answer": "B",
        "reasoning": "Kafka assigns each partition to exactly one consumer in a group (no sharing). With 6 partitions and 4 consumers, the balancer distributes as evenly as possible: 6 ÷ 4 = 1 remainder 2, so 2 consumers get 2 partitions and 2 consumers get 1 partition. No partitions are skipped.",
    },
    {
        "section": "Big Data",
        "question": "Kafka's 'at-least-once' delivery semantic can cause a downstream ML feature store to receive duplicate events. Which architectural choice most directly mitigates this?",
        "type": "mcq",
        "options": {
            "A": "Increasing the number of topic partitions",
            "B": "Using a shorter retention period",
            "C": "Idempotent writes keyed on a unique event ID",
            "D": "Switching the producer to asynchronous acknowledgment",
        },
        "answer": "C",
        "reasoning": "Idempotency means processing the same event multiple times produces the same result as processing it once. By keying writes on a unique event ID, the feature store can detect and discard duplicates. This directly addresses the at-least-once duplication problem regardless of how many times an event is delivered.",
    },
    {
        "section": "Big Data",
        "question": "You need to find the 100 most similar items to a query embedding out of 50 million candidates. Which of the following best describes the core mechanism that makes ANN (Approximate Nearest Neighbor) fast?",
        "type": "mcq",
        "options": {
            "A": "ANN compresses each embedding to 1 bit using locality-sensitive hashing, making distance computation exact but cheap",
            "B": "ANN indexes embeddings into structures (e.g., HNSW graphs or inverted indexes) that allow the search to skip most candidates and only evaluate a small promising subset",
            "C": "ANN retrains the embedding model to cluster similar items at adjacent memory addresses",
            "D": "ANN performs an exhaustive search but distributes the computation across GPUs to meet latency targets",
        },
        "answer": "B",
        "reasoning": "HNSW (Hierarchical Navigable Small World graphs) and inverted file indexes let ANN navigate directly to the neighborhood of the query vector, evaluating only a tiny fraction of the 50M candidates. This achieves sub-linear search time by trading a small amount of recall (not guaranteed exact results) for dramatic speed gains.",
    },
    {
        "section": "Big Data",
        "question": "In collaborative filtering, why does a two-tower model partially address the 'cold start' problem?",
        "type": "mcq",
        "options": {
            "A": "It eliminates the need for user history by relying on item metadata alone",
            "B": "It encodes users and items into separate embedding spaces using available features, allowing inference even with sparse history",
            "C": "It solves cold start by training on synthetic user profiles",
            "D": "It clusters users into groups and assigns the group's embedding to new members",
        },
        "answer": "B",
        "reasoning": "Traditional collaborative filtering requires interaction history and fails completely for new users/items. Two-tower models encode users and items using their *features* (age, location, item category, etc.) in separate towers. Even with zero interaction history, the feature-based embedding still produces a useful representation for inference.",
    },
    {
        "section": "Big Data",
        "question": "In a multi-stage recommendation pipeline, why is it architecturally important to separate candidate generation from the ranking stage?",
        "type": "mcq",
        "options": {
            "A": "The ranking model cannot generalize to unseen items without pre-filtering",
            "B": "A single ranker applied to millions of items would be computationally infeasible at serving latency",
            "C": "Candidate generation is always more accurate than ranking",
            "D": "Regulators require separation of retrieval and ranking for recommendation systems",
        },
        "answer": "B",
        "reasoning": "A heavy neural ranker scoring 10M+ items per request would take seconds — far exceeding acceptable latency budgets. Candidate generation (e.g., ANN retrieval) quickly narrows the field to ~100-1000 items using lightweight models, then the expensive ranker only runs on that small set, making real-time serving feasible.",
    },
    {
        "section": "Big Data",
        "question": "In the Markov Decision Process framework applied to recommendations, what does the 'state' typically represent?",
        "type": "mcq",
        "options": {
            "A": "The item currently being recommended",
            "B": "A summary of the user's interaction history and context at a given time",
            "C": "The reward signal from the last interaction",
            "D": "The set of all items available in the catalog",
        },
        "answer": "B",
        "reasoning": "In MDP, the 'state' must capture all information needed to decide the next optimal action. In a recommender system, this is the user's full context: their interaction history, preferences, current session, time of day, etc. A single item or reward alone is insufficient to represent the state.",
    },
    {
        "section": "Big Data",
        "question": "Tabular Q-learning maintains a lookup table of Q-values indexed by (state, action) pairs. Why does this approach fail in large-scale recommender systems?",
        "type": "mcq",
        "options": {
            "A": "The Q-table converges too quickly and overfits to the training data",
            "B": "The state and action spaces are so large that storing and updating a full Q-table is computationally and memory infeasible",
            "C": "Tabular Q-learning cannot handle discrete action spaces",
            "D": "It requires a differentiable reward function",
        },
        "answer": "B",
        "reasoning": "With millions of users (states) and millions of items (actions), the Q-table would have millions × millions = trillions of entries — impossible to store or update. Deep RL (e.g., DQN) replaces the table with a neural network that generalizes across similar states and actions.",
    },
    {
        "section": "Big Data",
        "question": "Free response: Choose any two of the following hashing use cases — consistent hashing, Bloom filters, Count-Min Sketch, Kafka partitioning — and explain: (a) the specific problem hashing solves, (b) why a naive alternative would be insufficient at scale, and (c) the key tradeoff introduced by using hashing.",
        "type": "free",
        "answer": (
            "**Consistent Hashing:** Solves routing of events to workers while minimizing remapping when cluster size changes. "
            "A naive mod-N hash requires remapping nearly all keys when a worker is added/removed (thundering-herd). "
            "Consistent hashing maps keys and workers to a ring — only keys between the departing and adjacent node must be remapped. "
            "Tradeoff: without virtual nodes, load distribution can be uneven; virtual nodes add implementation complexity.\n\n"
            "**Bloom Filters:** Tests set membership in O(1) time and constant memory. "
            "A naive hash set requires O(n) memory proportional to the number of elements. "
            "A Bloom filter achieves near-zero memory per element by sacrificing exactness — false positives are possible and deletions are not supported. "
            "Tradeoff: controllable via bits-per-element and number of hash functions."
        ),
        "reasoning": "",
    },
    # ── MACHINE LEARNING ─────────────────────
    {
        "section": "Machine Learning",
        "question": "For binary y ∈ {0,1}, a regression of y on x estimates E[y | x]. Why does this quantity equal a probability?",
        "type": "mcq",
        "options": {
            "A": "The regression forces fitted values between 0 and 1 by construction.",
            "B": "E[y | x] = 1·P(y=1|x) + 0·P(y=0|x), so the expected value of a 0-1 variable equals P(y=1|x).",
            "C": "The regression computes the sample mean of y, and sample means are always probabilities for categorical variables.",
            "D": "The expected value of any variable with finite support equals the probability of its maximum value.",
            "E": "E[y|x] is a probability only when logistic regression is used via a logit link.",
        },
        "answer": "B",
        "reasoning": "By the definition of expected value for a discrete variable: E[y|x] = 1·P(y=1|x) + 0·P(y=0|x) = P(y=1|x). This is a mathematical identity — not a modeling assumption — and holds regardless of what regression method is used.",
    },
    {
        "section": "Machine Learning",
        "question": "Define odds and interpret exp(βⱼ) in logistic regression.",
        "type": "mcq",
        "options": {
            "A": "Odds are 1−p, and exp(βⱼ) is the additive change in probability for a one-unit increase in xⱼ.",
            "B": "Odds are p/(1−p), and exp(βⱼ) is the factor by which the odds are multiplied for a one-unit increase in xⱼ.",
            "C": "Odds are p, and exp(βⱼ) is the probability multiplier for a one-unit increase in xⱼ.",
            "D": "Odds are (1−p)/p, and exp(βⱼ) is the odds multiplier for a one-unit decrease in xⱼ.",
            "E": "Odds are p/(1−p), and exp(βⱼ) is the derivative of p with respect to xⱼ at p=0.5.",
        },
        "answer": "B",
        "reasoning": "Odds = p/(1−p), the ratio of success to failure probability. In logistic regression: log(odds) = Xβ, so a one-unit increase in xⱼ increases log-odds by βⱼ, which means the odds are *multiplied* by exp(βⱼ). This is the **odds ratio** — the core interpretation of logistic regression coefficients.",
    },
    {
        "section": "Machine Learning",
        "question": "State the key identifying assumption behind diff-in-diff in plain language.",
        "type": "mcq",
        "options": {
            "A": "Treated and control outcomes must be identical in levels in all pre-treatment periods.",
            "B": "Absent treatment, the treated group would have experienced the same change in outcomes over time as the control group — the parallel trends assumption.",
            "C": "Treatment must be randomized within each time period.",
            "D": "The treatment effect must be constant across all units in every period.",
            "E": "There must be no aggregate time shocks in the post period affecting treated and control differently.",
        },
        "answer": "B",
        "reasoning": "DiD doesn't require the groups to have the same *level* of outcomes before treatment — just the same *trend*. The parallel trends assumption says: 'If treatment had never happened, both groups would have moved in parallel.' This allows us to use the control group's post-period change as the counterfactual for the treated group.",
    },
    {
        "section": "Machine Learning",
        "question": "What is a confounder and how does controlling in regression address confounding in principle?",
        "type": "mcq",
        "options": {
            "A": "A confounder is any variable correlated with y; controlling means dropping it from the regression.",
            "B": "A confounder is any variable correlated with treatment d; controlling means centering d around zero.",
            "C": "A confounder affects y and is correlated with d; controlling means conditioning on it so identification uses variation in d net of controls.",
            "D": "A confounder is always an unobserved variable; controlling means using robust standard errors.",
            "E": "A confounder is a post-treatment variable; controlling removes intermediate causal pathways.",
        },
        "answer": "C",
        "reasoning": "A confounder must both (1) affect the outcome Y and (2) be correlated with the treatment d. Including it in the regression conditions on it, so the remaining variation in d is as-good-as-random with respect to that confounder. This lets us isolate d's causal effect on Y, net of the confounder's influence.",
    },
    {
        "section": "Machine Learning",
        "question": "For the logistic model η = −0.8 + 0.4x₁ − 1.2x₂ with x₁ = 2, x₂ = 1, what are η and p?",
        "type": "mcq",
        "options": {
            "A": "η = −1.2 and p = 1/(1+e⁻¹·²)",
            "B": "η = 1.2 and p = 1/(1+e¹·²)",
            "C": "η = −0.4 and p = 1/(1+e⁰·⁴)",
            "D": "η = −1.2 and p = 1/(1+e¹·²), because −η = 1.2 enters the exponent in the inverse-logit formula.",
            "E": "η = −2.0 and p = 1/(1+e²·⁰)",
        },
        "answer": "D",
        "reasoning": "Compute η: −0.8 + 0.4(2) − 1.2(1) = −0.8 + 0.8 − 1.2 = **−1.2**. Then apply the inverse-logit: p = 1/(1+e^(−η)) = 1/(1+e^(−(−1.2))) = 1/(1+e^**1.2**). So η = −1.2 and the exponent in the denominator is +1.2.",
    },
    {
        "section": "Machine Learning",
        "question": "What is the relevance condition for an instrumental variable Z, and what problem arises when it fails?",
        "type": "mcq",
        "options": {
            "A": "Z must be uncorrelated with the error term; failure means the instrument is invalid.",
            "B": "Z must strongly predict the endogenous regressor X in the first stage; weak instruments cause large standard errors and bias toward OLS.",
            "C": "Z must affect Y only through X; failure means the exclusion restriction is violated.",
            "D": "Z must be randomly assigned; failure means the instrument picks up selection bias.",
            "E": "Z must have the same sign effect on X as X has on Y; failure means the IV estimate has the wrong sign.",
        },
        "answer": "B",
        "reasoning": "Relevance requires Z to be a strong predictor of X (high first-stage F-statistic, typically >10). With a weak instrument, the IV estimator inherits most of the OLS bias and standard errors blow up, making inference unreliable. Note: the exclusion restriction (option C) is the *validity* condition, not the relevance condition.",
    },
    {
        "section": "Machine Learning",
        "question": "Free response: Why might an autoencoder learn features that are not very helpful for a later classification task?",
        "type": "free",
        "answer": (
            "An autoencoder's training objective is **reconstruction**, which need not preserve the information most useful for predicting the target. "
            "The encoder retains whatever signal helps decode the input back out — even if that signal is unrelated to the class label."
        ),
        "reasoning": "",
    },
    # ── CAUSAL INFERENCE ─────────────────────
    {
        "section": "Causal Inference (Triple I)",
        "question": "Which of the following is true of the non-parametric approach to modeling treatment doses, compared to the parametric approach?",
        "type": "mcq",
        "options": {
            "A": "The non-parametric approach will typically have a lower R² than the parametric approach.",
            "B": "The non-parametric approach is better for forecasting Y for values of X not previously observed.",
            "C": "The non-parametric approach is more likely to lead to overfitting.",
        },
        "answer": "C",
        "reasoning": "Non-parametric models impose no structural assumptions and are highly flexible — they can fit the observed data very closely. This flexibility is a double-edged sword: without regularization or sufficient data, the model memorizes noise rather than learning the true relationship (overfitting). Parametric models impose constraints that act as regularization.",
    },
    {
        "section": "Causal Inference (Triple I)",
        "question": "Compared to laboratory experiments, field experiments have:",
        "type": "mcq",
        "options": {
            "A": "Higher external validity",
            "B": "Higher internal validity",
            "C": "Greater profitability",
        },
        "answer": "A",
        "reasoning": "Field experiments occur in real-world settings with actual subjects behaving naturally, making results more generalizable (high **external validity**). Lab experiments have greater control over confounders (high **internal validity**) but subjects may behave differently from how they would in the real world.",
    },
    {
        "section": "Causal Inference (Triple I)",
        "question": "Which of the following statements applies to observational data in which multiple units receive treatment at different times? (Select ALL that apply.)",
        "type": "multi",
        "options": {
            "A": "We cannot estimate a treatment effect because everyone in our sample receives treatment.",
            "B": "A two-way fixed effect model would be appropriate for this type of data.",
            "C": "This type of data is an example of 'staggered treatment.'",
        },
        "answer": ["B", "C"],
        "reasoning": "When units adopt treatment at different times, this is called **staggered treatment** (C). The units not yet treated serve as controls, so treatment effects can still be estimated (A is false). Two-way fixed effects (unit FE + time FE) is the standard econometric approach for this design (B).",
    },
    {
        "section": "Causal Inference (Triple I)",
        "question": "Which of the following may happen when a store implements a temporary discount? (Select ALL that apply.)",
        "type": "multi",
        "options": {
            "A": "A 'post-promotion dip.'",
            "B": "Stockpiling.",
            "C": "An increase in consumption that is not stockpiled.",
        },
        "answer": ["A", "B", "C"],
        "reasoning": "All three can occur. **Stockpiling (B):** consumers buy more than needed now at the lower price. **Post-promotion dip (A):** because consumers stockpiled during the promotion, demand falls below normal afterwards. **Genuine consumption increase (C):** some consumers actually use more of the product at the lower price, not just storing it.",
    },
    {
        "section": "Causal Inference (Triple I)",
        "question": "We have a categorical variable for educational attainment with five values (No degree, HS, College, Master's, PhD). How would we utilize this variable in a regression?",
        "type": "mcq",
        "options": {
            "A": "Create five dummy variables, one for each value",
            "B": "Create dummy variables for each reference value only",
            "C": "Create four dummy variables, for all but one value",
        },
        "answer": "C",
        "reasoning": "With k categories, include **k−1** dummy variables. The omitted category becomes the reference group whose effect is captured by the intercept. Including all k dummies creates perfect multicollinearity with the intercept (the **dummy variable trap**), making the model inestimable. With 5 levels → 4 dummies.",
    },
    {
        "section": "Causal Inference (Triple I)",
        "question": "Free response: You have completed an experiment and found a statistically significant result. Is the likelihood that your significant discovery is false the same as your significance level alpha?",
        "type": "free",
        "answer": (
            "**No, it is not.** The significance level α is the probability of rejecting the null *given the null is true* — P(reject H₀ | H₀ true). "
            "What you want to know after a significant result is P(H₀ true | reject H₀). "
            "P(A|B) is not necessarily equal to P(B|A)."
        ),
        "reasoning": "",
    },
    {
        "section": "Causal Inference (Triple I)",
        "question": "Free response: Define or explain endogeneity.",
        "type": "free",
        "answer": (
            "**Endogeneity** is when X is correlated with the error term. "
            "This arises when there is an omitted confounder — something that influences both X and Y. "
            "It can also arise from simultaneity, where X influences Y and Y influences X."
        ),
        "reasoning": "",
    },
    # ── ADVANCED STATISTICS ──────────────────
    {
        "section": "Advanced Statistics",
        "question": "Principal Components Regression is a supervised learning approach.",
        "type": "tf",
        "answer": "True",
        "reasoning": "PCR has two steps: (1) PCA — unsupervised dimensionality reduction to find principal components, then (2) Regression — supervised prediction of an outcome Y using those components. Because the final goal is predicting a labeled outcome Y, PCR is classified as a **supervised** learning method overall.",
    },
    {
        "section": "Advanced Statistics",
        "question": "A variance inflation factor (VIF) of unity indicates that the predictors are perfectly correlated.",
        "type": "tf",
        "answer": "False",
        "reasoning": "VIF = 1 means **no multicollinearity** — the predictor is completely orthogonal (uncorrelated) to all other predictors. VIF increases with collinearity; VIF > 10 is typically concerning. Perfect multicollinearity would cause VIF → ∞, not VIF = 1.",
    },
    {
        "section": "Advanced Statistics",
        "question": "A high curvature in the sum of squared errors function of a linear regression model means the estimated coefficient is insignificantly different from zero.",
        "type": "tf",
        "answer": "True",
        "reasoning": "High curvature in the SSE surface near the minimum means the loss is very sensitive to changes in the coefficient — the minimum is sharply defined, indicating a precise estimate. However, in the context of this course, a flat (low-curvature) SSE suggests the coefficient is poorly identified and insignificant. High curvature signals significance. (Note: interpret per course materials.)",
    },
    {
        "section": "Advanced Statistics",
        "question": "The AIC score for model A was −200, and that for model B was −204. Hence, model B should be retained.",
        "type": "tf",
        "answer": "True",
        "reasoning": "AIC (Akaike Information Criterion) measures relative model quality — **lower is better**. Since −204 < −200, model B has a lower AIC and is preferred. AIC penalizes model complexity, so B achieves better fit relative to its complexity.",
    },
    {
        "section": "Advanced Statistics",
        "question": "The prices in a conjoint experiment were $10 or $50, and the estimated price coefficient was minus 10. Hence, one util is worth $400.",
        "type": "tf",
        "answer": "False",
        "reasoning": "In conjoint analysis, the dollar value of one util = price range ÷ utility range from price. Price range = $50 − $10 = $40. Utility range from price = |−10| × (50 − 10) = 400 utils. So 1 util = $40/400 = **$0.10**, not $400. The answer reverses numerator and denominator.",
    },
    # ── INTERMEDIATE STATISTICS ──────────────
    {
        "section": "Intermediate Statistics",
        "question": "The log-log regression equation is: Estimated log REV = 7.1 + 2.4 · log ADV. Interpret the slope b₁ = 2.4.",
        "type": "mcq",
        "options": {
            "A": "For every 1% increase in REV, ADV increases by 2.4% on average.",
            "B": "For every 1% increase in ADV, REV increases by 7.1% on average.",
            "C": "For every 1% increase in ADV, REV increases by 2.4% on average.",
            "D": "For every 2.4% increase in REV, ADV increases by 7.1% on average.",
        },
        "answer": "C",
        "reasoning": "In a log-log model, the slope is the **elasticity**: a 1% increase in the X variable leads to a β₁% increase in the Y variable. Here, β₁ = 2.4, so a 1% increase in ADV → 2.4% increase in REV. The intercept (7.1) is irrelevant to the slope interpretation.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "Regression equations only represent linear trends in data.",
        "type": "tf",
        "answer": "False",
        "reasoning": "The word 'linear' in linear regression refers to linearity in the **parameters** (coefficients), not the predictors. By including log(x), x², interaction terms, or other transformations, regression can model curved, exponential, and other non-linear relationships between variables.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "In the model ŷ = β₀ + β₁ ln(x), what is the impact of the estimated slope coefficient β₁?",
        "type": "mcq",
        "options": {
            "A": "β₁ measures the approximate change in ŷ when x increases by 1 unit.",
            "B": "β₁ · 0.01 measures the approximate change in ŷ when x increases by 1%.",
            "C": "β₁ measures the approximate change in ŷ when x increases by 1%.",
            "D": "β₁ · 100 measures the approximate change in ŷ when x increases by 1 unit.",
        },
        "answer": "B",
        "reasoning": "Since d(ln x) ≈ Δx/x, a 1% increase in x means Δx/x = 0.01, so Δ(ln x) ≈ 0.01. Therefore Δŷ = β₁ · Δ(ln x) ≈ β₁ · 0.01. A common shorthand: β₁/100 is the change in ŷ per 1% increase in x.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "A nonlinear regression model where both the response and predictor variables are transformed into natural logs is called a:",
        "type": "mcq",
        "options": {
            "A": "Logistic regression model",
            "B": "Log-transformed model",
            "C": "Log-log regression model",
            "D": "Linear probability regression model",
        },
        "answer": "C",
        "reasoning": "When BOTH variables are log-transformed (log Y on log X), the model is called a **log-log** (or double-log) regression. The coefficient β₁ represents the elasticity. A 'log-transformed model' typically refers to only one variable being logged (semi-log). Logistic regression is for binary outcomes.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "Which of the following statements about Adjusted R² is FALSE?",
        "type": "mcq",
        "options": {
            "A": "It is possible to increase Adjusted R² unintentionally by including a predictor variable that has no foundation in the model.",
            "B": "Adjusted R² explicitly accounts for the sample size n and the number of predictor variables k.",
            "C": "Adjusted R² imposes a penalty for any additional predictor variable that is included in the analysis.",
            "D": "In models with the same response variable, the model with the higher Adjusted R² is preferred.",
        },
        "answer": "A",
        "reasoning": "Statement A is **false** — this is exactly the problem Adjusted R² was designed to solve. Unlike regular R², Adjusted R² only increases when a new variable improves the model *more than expected by chance*. Adding a useless predictor will decrease or leave unchanged the Adjusted R², not increase it.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "The dummy variable trap means:",
        "type": "mcq",
        "options": {
            "A": "Dropping the base group",
            "B": "Missing dummy variable",
            "C": "Using 1/−1 coding",
            "D": "Using all categories causes perfect collinearity",
        },
        "answer": "D",
        "reasoning": "If you create a dummy for every category, the sum of all dummies equals 1 for every observation — identical to the intercept column. This creates **perfect multicollinearity** with the constant term, making the design matrix singular and the OLS system unsolvable. The fix: drop one category (the reference group).",
    },
    {
        "section": "Intermediate Statistics",
        "question": "Heteroscedasticity means that:",
        "type": "mcq",
        "options": {
            "A": "All X variables cannot be assumed to be homogenous",
            "B": "The variance of the error term is not constant",
            "C": "The observed units have no relation",
            "D": "X and Y are not correlated",
        },
        "answer": "B",
        "reasoning": "Heteroscedasticity = 'different spread.' It means Var(εᵢ) is not constant across observations — error variance changes with X or other factors. This violates the classical OLS assumption of homoscedasticity. OLS estimates remain unbiased but standard errors become invalid, affecting hypothesis tests and confidence intervals.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "Which of the following measures is NOT suitable for out-of-sample forecasting?",
        "type": "mcq",
        "options": {"A": "AIC", "B": "BIC", "C": "R²", "D": "All of the above"},
        "answer": "C",
        "reasoning": "R² is purely an **in-sample** measure of fit — it always increases (or stays the same) when more variables are added, even useless ones. It cannot be meaningfully applied to out-of-sample data. AIC and BIC penalize complexity and approximate expected out-of-sample performance, making them better (though imperfect) for model selection for prediction.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "The Wilcoxon signed-rank sum test involves:",
        "type": "mcq",
        "options": {
            "A": "Calculating the difference between the sample data for each matched pair.",
            "B": "Ranking the absolute values of the (nonzero) differences from smallest to largest.",
            "C": "Attaching to each rank the sign of the original difference and computing the test statistic T.",
            "D": "All of the above",
        },
        "answer": "D",
        "reasoning": "The Wilcoxon signed-rank test is a sequential procedure: (A) compute differences for each pair and remove zeros, (B) rank the absolute values of those differences, and (C) reattach the original signs to the ranks and sum them to get the test statistic T. All three steps are integral parts of the test.",
    },
    {
        "section": "Intermediate Statistics",
        "question": "When comparing R² of two regression models, the models should have the same:",
        "type": "mcq",
        "options": {"A": "X variables", "B": "Y variables", "C": "Error term", "D": "Beta coefficients"},
        "answer": "B",
        "reasoning": "R² measures the proportion of variance in **Y** explained by the model. If two models predict different Y variables, their R² values measure proportions of completely different quantities and are not comparable. The X variables can differ — that's the whole point of comparing models.",
    },
    # ── FOUNDATIONS ──────────────────────────
    {
        "section": "Foundations",
        "question": "Which of the following is an example of a matched pairs design?",
        "type": "mcq",
        "options": {
            "A": "Comparing restaurant profit from 10 days without vs. 10 days during a campaign.",
            "B": "25 participants drive a Honda Civic for 1 week; another 25 drive a Toyota Camry for 1 week; both report MPG.",
            "C": "10 pairs of shoes — one soled with current material, one with new material — given to 10 participants to wear for 1 month.",
            "D": "10 tour guides get Samsonite bags; 10 others get American Tourister bags; rated after 6 months.",
        },
        "answer": "C",
        "reasoning": "A matched pairs (paired) design has each subject serve as their own control. In option C, each participant wears *both* shoe types simultaneously — one on each foot. This perfectly controls for individual differences in walking habits, weight, etc. Options B and D use independent groups with no pairing.",
    },
    {
        "section": "Foundations",
        "question": "If the probability of a Type I error is set at 0.05, then the probability of a Type II error will be 0.95.",
        "type": "tf",
        "answer": "False",
        "reasoning": "Type I error (α) and Type II error (β) are **not** complementary — they don't sum to 1. α = P(reject H₀ | H₀ true), while β = P(fail to reject H₀ | H₀ false). β depends on sample size, effect size, and power (1−β). You can reduce both simultaneously by increasing sample size.",
    },
    {
        "section": "Foundations",
        "question": "What test is an appropriate substitute for ANOVA if its assumptions cannot be met?",
        "type": "mcq",
        "options": {"A": "t", "B": "z", "C": "Spearman Rank Correlation", "D": "Kruskal-Wallis"},
        "answer": "D",
        "reasoning": "The **Kruskal-Wallis** test is the non-parametric equivalent of one-way ANOVA. It tests whether samples come from the same distribution using ranks instead of raw values, requiring no normality assumption. Spearman is for correlation; t and z test means for two groups, not multiple.",
    },
    {
        "section": "Foundations",
        "question": "When comparing two sample means, will the width of the Tukey confidence interval be wider, shorter, or the same as the standard two-population confidence interval?",
        "type": "mcq",
        "options": {"A": "Same", "B": "Wider", "C": "Shorter"},
        "answer": "B",
        "reasoning": "Tukey's method controls the **family-wise error rate** — the probability of making even one Type I error across *all* pairwise comparisons simultaneously. To maintain the overall α level across multiple comparisons, each individual interval must be wider than a standard two-sample CI (which only controls error for a single comparison).",
    },
    {
        "section": "Foundations",
        "question": "The chi-squared test of independence only detects linear association between variables in a contingency table.",
        "type": "tf",
        "answer": "False",
        "reasoning": "The chi-squared test of independence detects **any** kind of association between categorical variables — linear, non-linear, U-shaped, etc. It tests whether the observed cell frequencies differ from what would be expected under independence, without assuming any particular shape of relationship.",
    },
    {
        "section": "Foundations",
        "question": "The paired-sample procedure is appropriate when samples are naturally paired and there is a reasonably large positive correlation between the pairs. In this case it results in narrower confidence intervals.",
        "type": "tf",
        "answer": "True",
        "reasoning": "When pairs are positively correlated, Var(d̄) = Var(X₁ − X₂) = σ₁² + σ₂² − 2ρσ₁σ₂. With positive ρ, the variance of the differences is *smaller* than the sum of the individual variances. This reduces the standard error, producing narrower confidence intervals and more powerful tests.",
    },
    {
        "section": "Foundations",
        "question": "The police estimated 12 major accidents/day on a 10-mile highway stretch. Which distribution applies for finding P(fewer than 8 accidents/day)?",
        "type": "mcq",
        "options": {"A": "Binomial", "B": "Poisson", "C": "Hypergeometric", "D": "Exponential"},
        "answer": "B",
        "reasoning": "The **Poisson distribution** models the count of rare, independent events occurring at a known constant rate over a fixed interval (time or space). Here: 12 accidents/day on a stretch of highway is a classic Poisson setup. Binomial requires a fixed number of trials; Exponential models waiting time between events, not counts.",
    },
    {
        "section": "Foundations",
        "question": "University officials say at least 70% of students support a fee increase. The 95% CI is [0.75, 0.85]. What conclusion can be drawn?",
        "type": "mcq",
        "options": {
            "A": "Seventy percent is not in the interval, so another sample is needed.",
            "B": "Seventy percent is not in the interval, so assume it will not be supported.",
            "C": "The interval estimate is above 70%, so infer that it will be supported.",
            "D": "Since this was not based on the population, no conclusion can be drawn.",
        },
        "answer": "C",
        "reasoning": "The entire 95% confidence interval [0.75, 0.85] lies **above** 70%. This means we are 95% confident the true proportion exceeds 70%, supporting the officials' claim. Since 70% is not in the interval, we can conclude support is higher than the threshold — not that more sampling is needed.",
    },
    {
        "section": "Foundations",
        "question": "A technician reduces the probability of Type I error from 0.5% to 0.1%. What effect will this have on the probability of Type II error?",
        "type": "mcq",
        "options": {
            "A": "The probability of Type II error will remain the same.",
            "B": "The probability of Type II error will also decrease.",
            "C": "The probability of Type II error will increase.",
            "D": "It cannot be determined from the information given.",
        },
        "answer": "C",
        "reasoning": "For a fixed sample size, there is an inherent **trade-off** between Type I (α) and Type II (β) errors. Making the test more conservative (lower α — harder to reject H₀) means you'll miss more true effects, increasing β. To reduce both simultaneously, you need a larger sample size.",
    },
    {
        "section": "Foundations",
        "question": "A 95% confidence interval can be used to reject the null hypothesis of a two-sided test at the 5% significance level if and only if:",
        "type": "mcq",
        "options": {
            "A": "A 95% CI includes the hypothesized value of the parameter.",
            "B": "A 95% CI does not include the hypothesized value of the parameter.",
            "C": "The null hypothesis is less than 0.025.",
            "D": "The null hypothesis includes sampling error greater than 0.025.",
        },
        "answer": "B",
        "reasoning": "A 95% CI and a two-sided α=5% hypothesis test are mathematically equivalent (duals). If the hypothesized null value falls **outside** the 95% CI, the data is inconsistent with that value at the 5% significance level → reject H₀. If it falls inside → fail to reject H₀. They always agree.",
    },
    # ── DATA MANAGEMENT ──────────────────────
    {
        "section": "Data Management",
        "question": "Your boss needs a specialization hierarchy reflecting the relation between EMPLOYEES and its subtypes. What type of relationship do you need to show?",
        "type": "mcq",
        "options": {"A": "1:1", "B": "m:n", "C": "1:n", "D": "1:m"},
        "answer": "A",
        "reasoning": "A specialization (ISA) hierarchy shows EMPLOYEES as a supertype with subtypes (e.g., Manager, Engineer, Intern). Each employee belongs to **exactly one** subtype, and each subtype instance corresponds to **exactly one** employee — making the relationship **1:1** between the supertype and each subtype.",
    },
    {
        "section": "Data Management",
        "question": (
            "A mattress store has TABLE1 (sales reps, primary key: vcode) and TABLE2 (mattresses sold, with vcode and mt_code). "
            "Which query returns all sales representatives that haven't closed a sale?"
        ),
        "type": "mcq",
        "options": {
            "A": "SELECT * FROM TABLE1 RIGHT JOIN TABLE2 ON TABLE1.vcode = TABLE2.vcode WHERE mt_code IS NOT NULL.",
            "B": "SELECT * FROM TABLE1 JOIN TABLE2 ON TABLE1.vcode = TABLE2.vcode WHERE mt_code IS NULL.",
            "C": "SELECT * FROM TABLE1 LEFT JOIN TABLE2 ON TABLE1.vcode = TABLE2.vcode WHERE mt_code IS NULL.",
            "D": "SELECT * FROM TABLE1 RIGHT JOIN TABLE2 ON TABLE1.vcode = TABLE2.vcode WHERE mt_code IS NULL.",
        },
        "answer": "D",
        "reasoning": "Per the answer key, option D is correct. The RIGHT JOIN keeps all records from TABLE2 (the right table). WHERE mt_code IS NULL filters for cases where there is no matching sale. Note: Option C (LEFT JOIN) is often considered the more intuitive solution for 'reps with no sales,' but the course answer key designates D.",
    },
    {
        "section": "Data Management",
        "question": (
            "A sports league uses ROW_NUMBER() in the WHERE clause to filter the top 3 teams:\n\n"
            "```sql\nWITH team_standings AS (\n"
            "  SELECT 'Eagles' as team, 12 as wins UNION ALL\n"
            "  SELECT 'Hawks', 10 UNION ALL\n"
            "  SELECT 'Tigers', 10 UNION ALL\n"
            "  SELECT 'Lions', 9 UNION ALL\n"
            "  SELECT 'Bears', 8\n)\n"
            "SELECT team, wins,\n"
            "  ROW_NUMBER() OVER (ORDER BY wins DESC, team) as row_num\n"
            "FROM team_standings\n"
            "WHERE row_num <= 3;\n```\n\n"
            "What will happen when this query is executed?"
        ),
        "type": "mcq",
        "options": {
            "A": "Throws an error",
            "B": "Returns all 5 teams",
            "C": "Returns Eagles, Hawks, Tigers",
            "D": "Returns Eagles, Hawks, Lions",
        },
        "answer": "A",
        "reasoning": "Window functions like ROW_NUMBER() are computed **after** WHERE is evaluated in SQL's logical processing order (FROM → WHERE → SELECT → window functions). Referencing a window function alias in the WHERE clause causes an error because it doesn't exist yet at that stage. The fix: wrap the query in a CTE or subquery, then filter on row_num.",
    },
    {
        "section": "Data Management",
        "question": "In college football, each division has many players and each division has many teams. What type of relationship is division in with players and teams?",
        "type": "mcq",
        "options": {
            "A": "Division is in a 1:m relationship with both team and players.",
            "B": "Division is in a 1:1 relationship with team but 1:m with players.",
            "C": "Division is in a 1:m relationship with team but 1:1 with players.",
            "D": "Division is in a 1:1 relationship with both team and players.",
        },
        "answer": "A",
        "reasoning": "The business rules explicitly state: each division has **many** players AND each division has **many** teams. One division → many teams (1:m); one division → many players (1:m). Both relationships are one-to-many from the division's perspective.",
    },
]

# ─────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────
def init_session():
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "graded_count" not in st.session_state:
        st.session_state.graded_count = 0
    if "total_seen" not in st.session_state:
        st.session_state.total_seen = 0
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = None
    if "is_correct" not in st.session_state:
        st.session_state.is_correct = None
    if "section_filter" not in st.session_state:
        st.session_state.section_filter = "All Sections"
    # Shuffled queue: guarantees every question appears once before reshuffling
    if "queue" not in st.session_state:
        pool = list(range(len(QUESTIONS)))
        random.shuffle(pool)
        st.session_state.queue = pool
        st.session_state.queue_pos = 0


def build_queue(active_pool):
    """Build (or rebuild) the shuffled queue from active_pool."""
    pool = active_pool.copy()
    random.shuffle(pool)
    st.session_state.queue = pool
    st.session_state.queue_pos = 0


# ─────────────────────────────────────────────
# MAIN APP
# ─────────────────────────────────────────────
def main():
    init_session()

    # ── Sidebar ──────────────────────────────
    with st.sidebar:
        st.title("🎓 MSBA 2026")
        st.caption("Comprehensive Exam Practice")
        st.divider()

        sections = ["All Sections"] + sorted(set(q["section"] for q in QUESTIONS))
        new_filter = st.selectbox("📚 Filter by Section", sections,
                                  index=sections.index(st.session_state.section_filter))
        if new_filter != st.session_state.section_filter:
            st.session_state.section_filter = new_filter
            active = get_active_pool(new_filter)
            if active:
                build_queue(active)
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.session_state.is_correct = None
            st.rerun()

        st.divider()
        # Round progress
        q_num = st.session_state.queue_pos + 1
        q_total = len(st.session_state.queue)
        st.caption(f"Question **{q_num}** of **{q_total}** in this round")
        st.progress(q_num / q_total)

        st.metric("✅ Score", f"{st.session_state.score} / {st.session_state.graded_count}")

        if st.session_state.graded_count > 0:
            pct = int(100 * st.session_state.score / st.session_state.graded_count)
            st.progress(pct / 100, text=f"{pct}% correct")

        st.divider()
        if st.button("🔀 Reset & Shuffle", use_container_width=True):
            for key in ["answered", "score", "graded_count", "total_seen",
                        "user_answer", "is_correct", "queue", "queue_pos"]:
                st.session_state.pop(key, None)
            st.rerun()

    # ── Active question pool ──────────────────
    active_pool = get_active_pool(st.session_state.section_filter)
    if not active_pool:
        st.warning("No questions in this section.")
        return

    # Rebuild queue if it contains indices outside the active pool
    # (e.g. after a section filter change that wasn't caught above)
    if not st.session_state.queue or \
            not all(i in active_pool for i in st.session_state.queue):
        build_queue(active_pool)
        st.session_state.answered = False
        st.session_state.user_answer = None
        st.session_state.is_correct = None

    current_q_idx = st.session_state.queue[st.session_state.queue_pos]
    q = QUESTIONS[current_q_idx]

    # ── Question display ──────────────────────
    st.markdown("### " + q["question"])
    st.divider()

    # ── Input / Result ────────────────────────
    if not st.session_state.answered:
        render_input(q)

        st.divider()
        col1, col2, col3 = st.columns([1.3, 1, 1])
        with col1:
            check_clicked = st.button("🔍 Check Answer", type="primary", use_container_width=True)
        with col2:
            skip_clicked = st.button("⏭️ Skip", use_container_width=True)
        with col3:
            back_clicked = st.button("⬅️ Back", use_container_width=True,
                                     disabled=st.session_state.queue_pos == 0)

        if skip_clicked:
            go_next(active_pool)
            st.rerun()

        if back_clicked:
            go_back()
            st.rerun()

        if check_clicked:
            submit_answer(q)
            if st.session_state.answered:
                st.rerun()

    else:
        render_result(q)
        st.divider()
        col1, col2 = st.columns([1.3, 1])
        with col1:
            if st.button("➡️ Next Question", type="primary", use_container_width=True):
                go_next(active_pool)
                st.rerun()
        with col2:
            if st.button("⬅️ Back", use_container_width=True,
                         disabled=st.session_state.queue_pos == 0):
                go_back()
                st.rerun()


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def get_active_pool(section_filter):
    if section_filter == "All Sections":
        return list(range(len(QUESTIONS)))
    return [i for i, q in enumerate(QUESTIONS) if q["section"] == section_filter]


def go_next(active_pool):
    """Advance to the next position in the shuffled queue.
    When the queue is exhausted, reshuffle for the next round."""
    next_pos = st.session_state.queue_pos + 1
    if next_pos >= len(st.session_state.queue):
        build_queue(active_pool)
    else:
        st.session_state.queue_pos = next_pos
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.is_correct = None


def go_back():
    """Go back to the previous question in the queue (if any)."""
    if st.session_state.queue_pos > 0:
        st.session_state.queue_pos -= 1
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.is_correct = None


def get_shuffled_option_keys(q, key_suffix):
    """Return option keys in a stable shuffled order for this queue position.
    The shuffle is cached so reruns don't re-randomize mid-question."""
    cache_key = f"opt_order_{key_suffix}"
    if cache_key not in st.session_state:
        keys = list(q["options"].keys())
        random.shuffle(keys)
        st.session_state[cache_key] = keys
    return st.session_state[cache_key]


def render_input(q):
    key_suffix = st.session_state.queue_pos  # unique per position in queue
    if q["type"] == "tf":
        choice = st.radio("Select your answer:", ["True", "False"],
                          key=f"tf_{key_suffix}", index=None)
        st.session_state.user_answer = choice

    elif q["type"] == "mcq":
        shuffled_keys = get_shuffled_option_keys(q, key_suffix)
        choice = st.radio("Select your answer:", shuffled_keys,
                          format_func=lambda k: f"{k}. {q['options'][k]}",
                          key=f"mcq_{key_suffix}", index=None)
        st.session_state.user_answer = choice

    elif q["type"] == "multi":
        st.caption("Select ALL that apply:")
        shuffled_keys = get_shuffled_option_keys(q, key_suffix)
        selected = []
        for k in shuffled_keys:
            v = q["options"][k]
            if st.checkbox(f"**{k}.** {v}", key=f"multi_{key_suffix}_{k}"):
                selected.append(k)
        st.session_state.user_answer = selected

    elif q["type"] == "free":
        st.info("✍️ Free-response question. Write your answer below, then click **Check Answer** to see the model answer.")
        response = st.text_area("Your answer:", height=150,
                                key=f"free_{key_suffix}",
                                placeholder="Type your answer here...")
        st.session_state.user_answer = response


def submit_answer(q):
    if q["type"] == "free":
        st.session_state.answered = True
        st.session_state.is_correct = None
        st.session_state.total_seen += 1
    elif q["type"] == "multi":
        if not st.session_state.user_answer:
            st.warning("Please select at least one option.")
        else:
            correct_set = set(q["answer"])
            given_set = set(st.session_state.user_answer)
            st.session_state.is_correct = correct_set == given_set
            st.session_state.answered = True
            st.session_state.total_seen += 1
            st.session_state.graded_count += 1
            if st.session_state.is_correct:
                st.session_state.score += 1
    else:
        if not st.session_state.user_answer:
            st.warning("Please select an answer.")
        else:
            st.session_state.is_correct = (st.session_state.user_answer == q["answer"])
            st.session_state.answered = True
            st.session_state.total_seen += 1
            st.session_state.graded_count += 1
            if st.session_state.is_correct:
                st.session_state.score += 1


def render_result(q):
    if q["type"] == "free":
        st.success("📖 Model Answer")
        st.markdown(q["answer"])

    elif q["type"] == "multi":
        correct_set = set(q["answer"])
        given_set = set(st.session_state.user_answer) if st.session_state.user_answer else set()
        if st.session_state.is_correct:
            st.success("✅ Correct! You selected all the right options.")
        else:
            st.error(f"❌ Incorrect. Correct answer(s): **{', '.join(sorted(correct_set))}**")
        for k, v in q["options"].items():
            if k in correct_set and k in given_set:
                st.markdown(f"✅ **{k}.** {v}")
            elif k in correct_set:
                st.markdown(f"✅ **{k}.** {v} ← correct")
            elif k in given_set:
                st.markdown(f"❌ **{k}.** {v}")
            else:
                st.markdown(f"⬜ **{k}.** {v}")

    else:
        correct = q["answer"]
        given = st.session_state.user_answer
        if st.session_state.is_correct:
            st.success(f"✅ Correct! The answer is **{correct}**.")
        else:
            st.error(f"❌ Incorrect. You selected **{given}** — correct answer is **{correct}**.")

        if q["type"] == "mcq":
            for k, v in q["options"].items():
                if k == correct:
                    st.markdown(f"✅ **{k}.** {v}")
                elif k == given:
                    st.markdown(f"❌ **{k}.** {v}")
                else:
                    st.markdown(f"⬜ **{k}.** {v}")
        else:
            st.markdown(f"Correct answer: **{correct}**")

    # ── Reasoning ────────────────────────────
    reasoning = q.get("reasoning", "")
    if reasoning:
        st.divider()
        st.markdown("💡 **Why this is the answer:**")
        st.info(reasoning)


if __name__ == "__main__":
    main()
