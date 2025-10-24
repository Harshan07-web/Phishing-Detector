from flask import Flask, request, render_template
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from C_src.C_a_preprocessing.txt_cleaner import clean_url
from C_src.C_a_preprocessing.feature_extraction import extract_url_features
from C_src.C_b_model.predict import predict_url
from C_src.C_c_untils.domain_correction import correct_domain
from C_src.C_c_untils.tips_recommendation import recommend_practices

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Prediction
            result = predict_url(url)
            corrected = correct_domain(url)
            tips = recommend_practices(result == "Phishing")
            return render_template("results.html", url=url, corrected=corrected, result=result, tips=tips)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
