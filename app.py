import streamlit as st
import random

st.set_page_config(
    page_title="MSBA 2026 Exam Practice",
    page_icon="🎓",
    layout="centered",
)

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
    },
    {
        "section": "Analytic Decision Making",
        "question": "In linear programming, constraints always define a convex set.",
        "type": "tf",
        "answer": "False",
    },
    {
        "section": "Analytic Decision Making",
        "question": "A maximization problem can always be defined as a minimization problem by multiplying each constraint by -1.",
        "type": "tf",
        "answer": "False",
    },
    {
        "section": "Analytic Decision Making",
        "question": "Which of the following is NOT a typical assumption of linear programming models?",
        "type": "mcq",
        "options": {"A": "Proportionality", "B": "Additivity", "C": "Certainty", "D": "Nonlinearity"},
        "answer": "D",
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
    },
    {
        "section": "Analytic Decision Making",
        "question": "Selling diapers vs. selling fast fashion: In the case of diapers, firms should apply revenue management (a form of markdown pricing).",
        "type": "tf",
        "answer": "False",
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
    },
    {
        "section": "Machine Learning",
        "question": "Free response: Why might an autoencoder learn features that are not very helpful for a later classification task?",
        "type": "free",
        "answer": (
            "An autoencoder's training objective is **reconstruction**, which need not preserve the information most useful for predicting the target. "
            "The encoder retains whatever signal helps decode the input back out — even if that signal is unrelated to the class label."
        ),
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
    },
    # ── ADVANCED STATISTICS ──────────────────
    {
        "section": "Advanced Statistics",
        "question": "Principal Components Regression is a supervised learning approach.",
        "type": "tf",
        "answer": "True",
    },
    {
        "section": "Advanced Statistics",
        "question": "A variance inflation factor (VIF) of unity indicates that the predictors are perfectly correlated.",
        "type": "tf",
        "answer": "False",
    },
    {
        "section": "Advanced Statistics",
        "question": "A high curvature in the sum of squared errors function of a linear regression model means the estimated coefficient is insignificantly different from zero.",
        "type": "tf",
        "answer": "True",
    },
    {
        "section": "Advanced Statistics",
        "question": "The AIC score for model A was −200, and that for model B was −204. Hence, model B should be retained.",
        "type": "tf",
        "answer": "True",
    },
    {
        "section": "Advanced Statistics",
        "question": "The prices in a conjoint experiment were $10 or $50, and the estimated price coefficient was minus 10. Hence, one util is worth $400.",
        "type": "tf",
        "answer": "False",
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
    },
    {
        "section": "Intermediate Statistics",
        "question": "Regression equations only represent linear trends in data.",
        "type": "tf",
        "answer": "False",
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
    },
    {
        "section": "Intermediate Statistics",
        "question": "Which of the following measures is NOT suitable for out-of-sample forecasting?",
        "type": "mcq",
        "options": {"A": "AIC", "B": "BIC", "C": "R²", "D": "All of the above"},
        "answer": "C",
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
    },
    {
        "section": "Intermediate Statistics",
        "question": "When comparing R² of two regression models, the models should have the same:",
        "type": "mcq",
        "options": {"A": "X variables", "B": "Y variables", "C": "Error term", "D": "Beta coefficients"},
        "answer": "B",
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
    },
    {
        "section": "Foundations",
        "question": "If the probability of a Type I error is set at 0.05, then the probability of a Type II error will be 0.95.",
        "type": "tf",
        "answer": "False",
    },
    {
        "section": "Foundations",
        "question": "What test is an appropriate substitute for ANOVA if its assumptions cannot be met?",
        "type": "mcq",
        "options": {"A": "t", "B": "z", "C": "Spearman Rank Correlation", "D": "Kruskal-Wallis"},
        "answer": "D",
    },
    {
        "section": "Foundations",
        "question": "When comparing two sample means, will the width of the Tukey confidence interval be wider, shorter, or the same as the standard two-population confidence interval?",
        "type": "mcq",
        "options": {"A": "Same", "B": "Wider", "C": "Shorter"},
        "answer": "B",
    },
    {
        "section": "Foundations",
        "question": "The chi-squared test of independence only detects linear association between variables in a contingency table.",
        "type": "tf",
        "answer": "False",
    },
    {
        "section": "Foundations",
        "question": "The paired-sample procedure is appropriate when samples are naturally paired and there is a reasonably large positive correlation between the pairs. In this case it results in narrower confidence intervals.",
        "type": "tf",
        "answer": "True",
    },
    {
        "section": "Foundations",
        "question": "The police estimated 12 major accidents/day on a 10-mile highway stretch. Which distribution applies for finding P(fewer than 8 accidents/day)?",
        "type": "mcq",
        "options": {"A": "Binomial", "B": "Poisson", "C": "Hypergeometric", "D": "Exponential"},
        "answer": "B",
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
    },
    # ── DATA MANAGEMENT ──────────────────────
    {
        "section": "Data Management",
        "question": "Your boss needs a specialization hierarchy reflecting the relation between EMPLOYEES and its subtypes. What type of relationship do you need to show?",
        "type": "mcq",
        "options": {"A": "1:1", "B": "m:n", "C": "1:n", "D": "1:m"},
        "answer": "A",
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
    },
]

# ─────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────
SECTION_COLORS = {
    "Analytic Decision Making": "#4F46E5",
    "Big Data": "#0891B2",
    "Machine Learning": "#7C3AED",
    "Causal Inference (Triple I)": "#B45309",
    "Advanced Statistics": "#059669",
    "Intermediate Statistics": "#DC2626",
    "Foundations": "#D97706",
    "Data Management": "#6D28D9",
}

def init_session():
    if "pool" not in st.session_state:
        pool = list(range(len(QUESTIONS)))
        random.shuffle(pool)
        st.session_state.pool = pool
        st.session_state.pool_idx = 0
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

def current_question():
    idx = st.session_state.pool[st.session_state.pool_idx % len(st.session_state.pool)]
    return QUESTIONS[idx]

def advance():
    st.session_state.pool_idx += 1
    if st.session_state.pool_idx >= len(st.session_state.pool):
        random.shuffle(st.session_state.pool)
        st.session_state.pool_idx = 0
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.is_correct = None


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
        st.session_state.section_filter = st.selectbox("📚 Filter by Section", sections)

        st.divider()
        st.metric("✅ Score", f"{st.session_state.score} / {st.session_state.graded_count}")
        st.metric("📖 Questions Seen", st.session_state.total_seen)

        if st.session_state.graded_count > 0:
            pct = int(100 * st.session_state.score / st.session_state.graded_count)
            st.progress(pct / 100, text=f"{pct}% correct")

        st.divider()
        if st.button("🔀 Reset & Shuffle", use_container_width=True):
            for key in ["pool", "pool_idx", "answered", "score", "graded_count",
                        "total_seen", "user_answer", "is_correct"]:
                st.session_state.pop(key, None)
            st.rerun()

    # ── Filter pool if section selected ──────
    section_filter = st.session_state.section_filter
    if section_filter != "All Sections":
        filtered_indices = [i for i, q in enumerate(QUESTIONS) if q["section"] == section_filter]
        active_pool = filtered_indices
    else:
        active_pool = list(range(len(QUESTIONS)))

    if not active_pool:
        st.warning("No questions in this section.")
        return

    # Pick a question from the filtered pool
    if "current_q_idx" not in st.session_state or not st.session_state.answered:
        if "current_q_idx" not in st.session_state:
            st.session_state.current_q_idx = random.choice(active_pool)
    q = QUESTIONS[st.session_state.current_q_idx]

    # ── Question ──────────────────────────────
    st.markdown("### " + q["question"])
    st.divider()

    # ── Input widget ──────────────────────────
    if not st.session_state.answered:
        if q["type"] == "tf":
            choice = st.radio(
                "Select your answer:",
                ["True", "False"],
                key=f"tf_{st.session_state.current_q_idx}",
                index=None,
            )
            st.session_state.user_answer = choice

        elif q["type"] == "mcq":
            labels = [f"**{k}.** {v}" for k, v in q["options"].items()]
            choice = st.radio(
                "Select your answer:",
                list(q["options"].keys()),
                format_func=lambda k: f"{k}. {q['options'][k]}",
                key=f"mcq_{st.session_state.current_q_idx}",
                index=None,
            )
            st.session_state.user_answer = choice

        elif q["type"] == "multi":
            st.caption("Select ALL that apply:")
            selected = []
            for k, v in q["options"].items():
                if st.checkbox(f"**{k}.** {v}", key=f"multi_{st.session_state.current_q_idx}_{k}"):
                    selected.append(k)
            st.session_state.user_answer = selected

        elif q["type"] == "free":
            st.info("✍️ This is a free-response question. Write your answer below, then click **Check Answer** to see the model answer.")
            response = st.text_area(
                "Your answer:",
                height=150,
                key=f"free_{st.session_state.current_q_idx}",
                placeholder="Type your answer here...",
            )
            st.session_state.user_answer = response

        # ── Check Answer / Skip buttons ───────
        st.divider()
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            check_clicked = st.button("🔍 Check Answer", type="primary", use_container_width=True)
        with col2:
            skip_clicked = st.button("⏭️ Skip", use_container_width=True)

        if skip_clicked:
            st.session_state.current_q_idx = random.choice(active_pool)
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.session_state.is_correct = None
            st.rerun()

        if check_clicked:
            if q["type"] == "free":
                st.session_state.answered = True
                st.session_state.is_correct = None  # self-graded
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
            if st.session_state.answered:
                st.rerun()

    # ── Result display ────────────────────────
    else:
        q = QUESTIONS[st.session_state.current_q_idx]

        if q["type"] == "free":
            st.success("📖 Model Answer")
            st.markdown(q["answer"])
            st.caption("Self-grade: was your answer on the right track?")

        elif q["type"] == "multi":
            correct_set = set(q["answer"])
            given_set = set(st.session_state.user_answer) if st.session_state.user_answer else set()
            if st.session_state.is_correct:
                st.success("✅ Correct! You selected all the right options.")
            else:
                st.error(f"❌ Incorrect. Correct answer(s): **{', '.join(sorted(correct_set))}**")
            st.markdown("**Your selection:** " + (", ".join(sorted(given_set)) if given_set else "_(none)_"))
            # Show all options with labels
            for k, v in q["options"].items():
                if k in correct_set:
                    st.markdown(f"✅ **{k}.** {v}")
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
                st.error(f"❌ Incorrect. You selected **{given}** — the correct answer is **{correct}**.")

            if q["type"] == "mcq":
                for k, v in q["options"].items():
                    if k == correct:
                        st.markdown(f"✅ **{k}.** {v}")
                    elif k == given:
                        st.markdown(f"❌ **{k}.** {v}")
                    else:
                        st.markdown(f"⬜ **{k}.** {v}")
            else:  # tf
                st.markdown(f"Correct answer: **{correct}**")

        # ── Next Question button ──────────────
        st.divider()
        if st.button("➡️ Next Question", type="primary", use_container_width=False):
            st.session_state.current_q_idx = random.choice(active_pool)
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.session_state.is_correct = None
            st.rerun()


if __name__ == "__main__":
    main()
