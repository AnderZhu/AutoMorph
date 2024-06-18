date
rm -rf ./Results/*
# STEP 1 IMAGE PREPROCESSING (EXTRA BACKGROUND REMOVE, SQUARE)

echo "### Preprocess Start ###"
cd M0_Preprocess
python EyeQ_process_main.py
