from flask import Flask, request, render_template, flash
import sys, os
import logging

# --- Add project path ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- Import internal modules ---
from C_src.C_a_preprocessing.txt_cleaner import clean_url
from C_src.C_a_preprocessing.feature_extraction import extract_url_features
from C_src.C_b_model.predict import predict_url
from C_src.C_c_untils.domain_correction import correct_domain
from C_src.C_c_untils.tips_recommendation import recommend_practices
from C_src.C_d_evaluation.evaluate import evaluate_model 

# --- Flask setup ---
app = Flask(__name__)
app.secret_key = "phishguard_secret"  # Needed for flash messages
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Main route: handles URL submission, prediction, correction, and tip generation.
    """
    if request.method == "POST":
        url = (request.form.get("url") or "").strip()

        if not url:
            flash("Please enter a URL to analyze.", "warning")
            return render_template("index.html")

        try:
            # --- Step 1: Clean and extract features ---
            cleaned_url = clean_url(url)
            features = extract_url_features(cleaned_url)

            # --- Step 2: Predict phishing or legitimate ---
            result_label,result_code,all_features = predict_url(cleaned_url)

            # --- Step 3: Smart domain correction ---
            corrected_domain, corrected_flag = correct_domain(cleaned_url)

            # --- Step 4: Generate context-aware tips ---
            tips = recommend_practices(features=all_features, predicted_label=result_code)

            # --- Step 5: Prepare context for rendering ---
            return render_template(
                "results.html",
                url=url,
                cleaned_url=cleaned_url,
                corrected=corrected_domain if corrected_flag else None,
                corrected_flag=corrected_flag,
                result=result_label,
                tips=tips,
            )

        except Exception as e:
            logging.error(f"Error processing URL: {e}")
            flash("An unexpected error occurred while analyzing the URL.", "danger")
            return render_template("index.html")

    return render_template("index.html")

@app.route("/evaluate", methods=["GET", "POST"])
def evaluate():
    """
    Route to evaluate model performance and display metrics.
    """
    try:
        model_path = r"D:\phishing Detector\D_saved_models\rf_model.pkl"
        test_data_path = r"D:\phishing Detector\A_data\Phishing_Legitimate.csv"  # update path if needed

        metrics = evaluate_model(model_path, test_data_path)

        return render_template("evaluation.html", metrics=metrics)
    except Exception as e:
        logging.error(f"Error during evaluation: {e}")
        flash("Model evaluation failed. Please check dataset and model files.", "danger")
        return render_template("index.html")

# --- Entry point ---
if __name__ == "__main__":
    app.run(debug=True)
