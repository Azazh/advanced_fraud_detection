

# Advanced Fraud Detection

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Azazh/advanced_fraud_detection)

This repository contains the implementation of **Advanced Fraud Detection**, a project aimed at detecting fraudulent transactions using machine learning techniques. The project focuses on data preprocessing, exploratory data analysis (EDA), feature engineering, and model preparation.



## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Folder Structure](#folder-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Key Findings](#key-findings)
8. [Contributing](#contributing)
9. [Contact](#contact)
10. [License](#license)



## Overview

Fraud detection is critical for businesses to minimize financial losses and improve customer trust. This project implements a pipeline for analyzing transaction data, identifying patterns of fraudulent behavior, and preparing the dataset for machine learning models. Key tasks include:

- Handling missing values and duplicates
- Cleaning and normalizing data
- Performing exploratory data analysis (EDA)
- Engineering features such as transaction frequency and time-to-action
- Preparing the dataset for downstream modeling


## Features

- **Data Preprocessing**: Handles missing values, removes duplicates, and corrects data types.
- **Feature Engineering**: Creates meaningful features like `time_to_action`, `transaction_frequency`, and geolocation-based features.
- **Normalization**: Scales numerical features for compatibility with machine learning algorithms.
- **Exploratory Data Analysis (EDA)**: Provides insights into class imbalance, fraud hotspots, and transaction patterns.
- **Modular Codebase**: Organized structure for scalability and reproducibility.



## Dataset

The dataset used in this project consists of transaction data with the following key attributes:

- **User Information**: `user_id`, `signup_time`, `purchase_time`, `device_id`, `age`, `sex`
- **Transaction Details**: `purchase_value`, `ip_address`, `country`
- **Labels**: Binary target variable (`class`) indicating whether a transaction is fraudulent (`1`) or legitimate (`0`).

The dataset is split into:
- **Raw Data**: Located in `data/raw/`
- **Processed Data**: Located in `data/processed/`



## Folder Structure

```
advanced_fraud_detection/
├── README.md                     # Project overview and setup instructions
├── CONTRIBUTING.md               # Guidelines for contributing to the project
├── LICENSE                       # License file (MIT)
├── CHANGELOG.md                  # Tracks changes, updates, and version history
├── .gitignore                    # Specifies files and directories to ignore in version control
├── requirements.txt              # Lists Python dependencies for the project
├── requirements-dev.txt          # Lists development-specific dependencies (e.g., pytest, flake8)
├── environment.yml               # Conda environment configuration (optional, if using Conda)
├── pyproject.toml                # Configuration for packaging and linting tools (e.g., Black, isort)
├── setup.py                      # Package setup file for distributing the project as a Python package
├── tests/                        # Unit tests and integration tests for the project
│   ├── unit/                     # Unit tests for individual components
│   └── integration/              # Integration tests for workflows and pipelines
├── src/                          # Source code for the project
│   ├── __init__.py               # Makes the src directory a Python package
│   ├── config.py                 # Configuration settings (e.g., file paths, hyperparameters)
│   ├── preprocessing.py          # Data cleaning, feature engineering, and transformation logic
│   ├── models.py                 # Model training, evaluation, and prediction logic
│   ├── utils.py                  # Helper/utility functions (e.g., logging, visualization)
│   └── pipeline.py               # End-to-end pipeline orchestration (data -> model -> deployment)
├── scripts/                      # Scripts for running workflows (e.g., data ingestion, model training)
│   ├── __init__.py               # Makes the scripts directory a Python package
│   ├── train_model.py            # Script to train and save the model
│   ├── evaluate_model.py         # Script to evaluate the model on test data
│   └── deploy_model.py           # Script for deploying the model (e.g., as an API)
├── notebooks/                    # Jupyter notebooks for exploratory data analysis (EDA) and experimentation
│   ├── EDA.ipynb                 # Exploratory data analysis notebook
│   ├── feature_engineering.ipynb # Feature engineering experiments
│   └── model_experiments.ipynb   # Model training and evaluation experiments
├── data/                         # Raw, processed, and intermediate data
│   ├── raw/                      # Raw datasets (e.g., Fraud_Data.csv, creditcard.csv)
│   ├── processed/                # Processed datasets after cleaning and feature engineering
│   └── interim/                  # Intermediate data files (optional, for debugging)
├── models/                       # Saved models and related artifacts
│   ├── trained_models/           # Final trained models (e.g., .pkl or .joblib files)
│   └── metrics/                  # Evaluation metrics (e.g., JSON or CSV files)
├── logs/                         # Logs for debugging and monitoring
│   ├── training_logs/            # Logs generated during model training
│   └── deployment_logs/          # Logs generated during model deployment
└── assets/                       # Static assets like images, diagrams, or visualizations
```



## Installation

### Prerequisites

- Python 3.9+
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Azazh/advanced_fraud_detection.git
   cd advanced_fraud_detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. (Optional) Set up a Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate advanced_fraud_detection
   ```



## Usage

### Run the Preprocessing Pipeline
To preprocess the raw data and generate the processed dataset:
```bash
python scripts/preprocess_data.py
```

### Perform Exploratory Data Analysis (EDA)
Open the `notebooks/EDA.ipynb` notebook to analyze the dataset and visualize key insights.

### Train a Model
To train a machine learning model:
```bash
python scripts/train_model.py
```

### Evaluate the Model
To evaluate the trained model:
```bash
python scripts/evaluate_model.py
```



## Key Findings

1. **Class Imbalance**:
   - Fraudulent transactions account for **9.37%** of the dataset.
   - Techniques like SMOTE or class weighting will be required during modeling.

2. **Geolocation Insights**:
   - High fraud rates are observed in countries such as **Nigeria**, **Russia**, and **Vietnam**.

3. **Time-to-Action**:
   - Fraudulent transactions occur significantly faster (**673.29 hours**) compared to legitimate transactions (**1,370.01 hours**).

4. **Transaction Frequency Issue**:
   - The `transaction_frequency` column currently shows **0.00** for all users, indicating a flaw in the calculation logic.


## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

For more details, refer to [CONTRIBUTING.md](CONTRIBUTING.md).



## Contact

For questions or feedback, feel free to reach out:

- Email: [azazhwuletaw@gmail.com](mailto:azazhwuletaw@gmail.com)
- GitHub: [@Azazh](https://github.com/Azazh)



## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details.


