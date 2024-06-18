# STEP 3 OPTIC DISC & VESSEL & ARTERY/VEIN SEG
echo "### Segmentation Modules ###"

cd M2_Vessel_seg
sh test_outside.sh

cd ../M2_Artery_vein
sh test_outside.sh

cd ../M2_lwnet_disc_cup
sh test_outside.sh

echo "### Done ###"


date
