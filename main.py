import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from C_src.C_a_preprocessing.txt_cleaner import clean_url
from C_src.C_a_preprocessing.feature_extraction import extract_url_features
from C_src.C_b_model.predict import predict_url
from C_src.C_c_untils.domain_correction import correct_domain
from C_src.C_c_untils.tips_recommendation import recommend_practices


url = "https://login.example.com@malicious.example.com/"

# --- SWAP THESE TWO LINES ---
# 1. PREDICT on the full, raw URL first.
result = predict_url(url) 

# 2. Get the "corrected" domain ONLY for display.
corrected = correct_domain(url)

tips = recommend_practices(result == "Phishing")

print(f"URL: {url}")
print(f"Corrected Domain: {corrected}")
print(f"Prediction: {result}") # This will now be correct
print("\nSafety Tips:")
for tip in tips:
    print("-", tip)