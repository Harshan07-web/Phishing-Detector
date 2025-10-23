import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from C_src.C_a_preprocessing.txt_cleaner import clean_url
from C_src.C_a_preprocessing.feature_extraction import extract_features
from C_src.C_b_model.predict import predict_url
from C_src.C_c_untils.domain_correction import correct_domain
from C_src.C_c_untils.tips_recommendation import recommend_practices


url = "https://secure-paypal-login.verify-account.com"
corrected = correct_domain(url)
result = predict_url(corrected)
tips = recommend_practices(result == "Phishing")

print(f"URL: {url}")
print(f"Corrected Domain: {corrected}")
print(f"Prediction: {result}")
print("\nSafety Tips:")
for tip in tips:
    print("-", tip)
