# Big Data Mining and Analytics - Project Exam

**Course**: DSC3108  
**Scenario**: Large-Scale Retail Recommendation System  
**Student**: GENO OWOR JOSHUA 
**REG NO.**: M23B23/006


## 📋 Project Overview

This project implements a scalable product recommendation system for an e-commerce platform using Apache Spark and the Alternating Least Squares (ALS) algorithm.

## 📁 Project Structure

```
Big Data Exam/
├── 1_data_generation.ipynb          # Generate synthetic retail data
├── 2_part_a_preprocessing.ipynb     # Part A: Setup & Preprocessing
├── 3_part_b_modeling.ipynb          # Part B: ALS Modeling & Analytics
├── 4_part_c_report.ipynb            # Part C: Report Content
├── products.csv                     # Generated product catalog
├── transactions.csv                 # Generated transaction data
└── README.md                        # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Java 8+ (for Spark)
- Jupyter Notebook

### Installation

```bash
# Install required packages
pip install pyspark numpy pandas jupyter

# Start Jupyter
jupyter notebook
```

### Execution Order

1. **Run `1_data_generation.ipynb`** - Generates synthetic datasets
2. **Run `2_part_a_preprocessing.ipynb`** - Part A (30 marks)
3. **Run `3_part_b_modeling.ipynb`** - Part B (40 marks)
4. **Review `4_part_c_report.ipynb`** - Part C content (30 marks)

## 📊 Dataset Details

- **Users**: 5,000 unique customers
- **Products**: 1,000 items across 5 categories
- **Transactions**: 200,000+ purchase records
- **Time Range**: 2024 (full year)

## 🎯 Project Milestones

### ✅ Milestone 1: Project Design & Implementation (30%)
- Big Data justification
- PySpark platform setup
- Data ingestion and cleaning
- Distributed preprocessing

### ✅ Milestone 2: Model Development & Analysis (40%)
- ALS algorithm implementation
- Model training and optimization
- Performance evaluation (RMSE)
- Recommendation generation

### ✅ Milestone 3: Report & Ethics (30%)
- Business application analysis
- Ethical implications discussion
- Privacy considerations
- Final presentation slides

## 🔑 Key Results

| Metric | Value |
|--------|-------|
| Dataset Size | 200,000+ transactions |
| Base Model RMSE | [Run notebooks to see] |
| Optimized Model RMSE | [Run notebooks to see] |
| Training Time | [Run notebooks to see] |

## 💼 Business Value

1. **Revenue Growth**: Cross-selling and upselling opportunities
2. **Customer Retention**: Personalized user experiences
3. **Inventory Optimization**: Demand forecasting and stock management

## ⚖️ Ethical Considerations

- **Privacy**: User data anonymization and GDPR compliance
- **Bias**: Mitigation of popularity bias in recommendations
- **Transparency**: Explainable recommendation logic
- **Fairness**: Balanced exposure for small sellers

## 📚 References

1. Spark MLlib Documentation
2. Hu, Y., Koren, Y., & Volinsky, C. (2008). Collaborative Filtering for Implicit Feedback Datasets
3. Uganda Data Protection and Privacy Act (2019)

## 📝 Submission Checklist

- [x] Jupyter notebooks with code and explanations
- [ ] Final PDF report (export from notebook 4)
- [ ] Presentation slides (8-10 slides)
- [ ] GitHub repository link (optional)

## 🔗 GitHub Repository

[Upload to your personal GitHub account and add link here]

---

**Note**: This project uses synthetic data for demonstration purposes. In production, real transaction data would be used with proper privacy safeguards.
