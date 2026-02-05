# Model Development Report
## Multi-Class Classification of Personality Types

---

## 1. Description

This report documents the training and development of four machine learning models for classifying 16 MBTI personality types using survey response data. The dataset contains 60 survey questions capturing personality traits, and the goal is to predict one of 16 personality types (INFP, INTJ, etc.).

---

## 2. Models Trained

| Model | Rationale |
|-------|-----------|
| **XGBoost (Gradient Boosting)** | Ensemble method that builds trees sequentially to correct errors, excellent for tabular data with complex patterns |
| **Random Forest** | Robust ensemble of decision trees using bagging; handles high-dimensional data well and provides feature importance |
| **Logistic Regression** | Linear baseline model with multinomial softmax; interpretable coefficients reveal feature relationships |
| **Linear Discriminant Analysis (LDA)** | Dimensionality reduction classifier; finds linear combinations that best separate classes |

---

## 3. Hyperparameter Choices

### XGBoost (Gradient Boosting)
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| n_estimators | 500 | Maximum trees (early stopping determines actual) |
| learning_rate | 0.1 | Standard rate balancing speed and precision |
| max_depth | 6 | Moderate depth to prevent overfitting |
| subsample | 0.8 | Row sampling for regularization |
| colsample_bytree | 0.8 | Feature sampling per tree |
| early_stopping_rounds | 15 | Stop if no improvement on validation set |

### Random Forest
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| n_estimators | 100 | Standard number of trees |
| max_depth | 20 | Deeper trees for complex patterns |
| min_samples_split | 5 | Minimum samples to split a node |
| min_samples_leaf | 2 | Minimum samples at leaf nodes |
| max_features | sqrt | Square root of features per split |

### Logistic Regression
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| multi_class | multinomial | Softmax for 16-class classification |
| solver | lbfgs | Efficient for multinomial problems |
| max_iter | 1000 | Ensure convergence |
| C | 1.0 | Default L2 regularization strength |

### Linear Discriminant Analysis
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| solver | svd | SVD solver (no matrix inversion needed) |
| n_components | None (15 used) | Uses min(n_classes-1, n_features) |
| tol | 1e-4 | Rank estimation threshold |

---

## 4. Training Iterations

| Model | Iterations/Trees | Notes |
|-------|------------------|-------|
| XGBoost | ~100-150 (early stopped from 500) | Early stopping on validation loss |
| Random Forest | 100 trees | Full ensemble trained |
| Logistic Regression | ~200-400 iterations | Converged before max_iter |
| LDA | Single pass | Analytical solution, no iterations |

---

## 5. Validation Strategy

**Stratified Hold-Out Split (70/15/15)**
- **Training Set:** 70% (~46,200 samples)
- **Validation Set:** 15% (~9,900 samples) — used for early stopping and model selection
- **Test Set:** 15% (~9,900 samples) — final unbiased evaluation
- **Stratification:** Maintained class proportions across all splits
- **Random State:** 42 (fixed for reproducibility)

All models used identical data splits to ensure fair comparison.

---

## 6. Training Results

| Model | Test Accuracy | Macro F1 | Training Accuracy | Gap |
|-------|---------------|----------|-------------------|-----|
| **XGBoost** | **98.22%** | 0.9822 | 99.95% | 1.73% |
| Random Forest | 97.57% | 0.9757 | 99.99% | 2.42% |
| Logistic Regression | 91.90% | 0.9189 | 92.04% | 0.14% |
| LDA | 90.56% | 0.9055 | 90.72% | 0.16% |

**Best Model:** XGBoost achieved the highest test accuracy (98.22%) with minimal overfitting.

---

## 7. Computational Resources

| Model | Training Time | Hardware |
|-------|---------------|----------|
| XGBoost | ~2-3 minutes | Multi-core CPU (n_jobs=-1) |
| Random Forest | ~1-2 minutes | Multi-core CPU (n_jobs=-1) |
| Logistic Regression | ~30-60 seconds | Multi-core CPU (n_jobs=-1) |
| LDA | ~5-10 seconds | Single-core (analytical) |

**Environment:** Python 3.x with scikit-learn, XGBoost libraries on standard desktop hardware.

---

## 8. Key Findings

1. **Ensemble methods outperform linear models** — XGBoost and Random Forest achieved >97% accuracy vs ~91% for linear models
2. **Gradient boosting is optimal** — XGBoost's sequential correction mechanism captures subtle personality patterns
3. **Linear models generalize better** — Smaller train-test gap (0.14% vs 1.7-2.4%) but lower overall accuracy
4. **All models trained efficiently** — Total training time under 5 minutes for all four models combined
