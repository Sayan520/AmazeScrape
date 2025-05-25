from flask import Flask, request, jsonify, render_template, send_file
from scraper.save import save_data, save_to_mysql
from scraper.scrape_amazon import scrape_amazon

# Initialize Flask application
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint to scrape Amazon data
@app.route("/api/scrape", methods=["POST"])
def scrape_api():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    try:
        data = request.get_json()
        query = data.get("query", "").strip()
        pages = int(data.get("pages", 1))
        fmt = data.get("format", "csv").lower()
        filename = data.get("filename", "output").strip().rstrip("_")

        if not query or pages < 1 or fmt not in ("csv", "xlsx"):
            return jsonify({"error": "Invalid input parameters"}), 400

        # Scrape data
        df = scrape_amazon(query, pages)

        # Save data to file
        file_path = save_data(df, filename, fmt)
        if not file_path:
            return jsonify({"error": "Failed to save file."}), 500

        # Send file as response
        response = send_file(
            file_path,
            as_attachment=True,
            download_name=f"{filename}.{fmt}"
        )
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
