# Setup Environment - Miniconda
conda create --name main-ds

conda activate main-ds

pip install -r requirements.txt

# Run Streamlit App
streamlit run web.py
