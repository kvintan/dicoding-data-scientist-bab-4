# Project Analysis Dashboard ✨

This project provides a data analysis solution using Jupyter Notebook and a web interface powered by Streamlit. The aim is to make data insights accessible and interactive, using visual tools and a simple web-based interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
  - [Setup with Anaconda](#setup-with-anaconda)
  - [Setup with Shell/Terminal](#setup-with-shellterminal)
- [Running the Project](#running-the-project)
  - [Data Analysis](#data-analysis)
  - [Streamlit Web Interface](#streamlit-web-interface)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Features](#features)
- [FAQ](#faq)
- [Getting Help](#getting-help)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project involves:
- **Data Analysis**: Using `Proyek_Analisis_Data.ipynb`, we analyze the dataset with Pandas, NumPy, and various visualization libraries to extract insights.
- **Web Interface**: `web.py` allows users to interact with the data via a Streamlit-powered web interface.

## Installation

### Setup with Anaconda

1. Create an isolated Conda environment:
   ```sh
   conda create --name data-env python=3.9
   conda activate data-env
   pip install -r requirements.txt
   ```

2. Setup with Shell/Terminal
   ```
   mkdir proyek_analisis_data
   cd proyek_analisis_data
   pipenv install
   pipenv shell
   pip install -r requirements.txt
   ```

3. Running the project
   ```
   jupyter notebook Proyek_Analisis_Data.ipynb
   streamlit run web.py
   ```
