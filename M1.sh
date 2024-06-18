# STEP 2 IMAGE QUALITY ASSESSMENT

echo "### Image Quality Assessment ###"

cd M1_Retinal_Image_quality_EyePACS
sh test_outside.sh

python merge_quality_assessment.py
