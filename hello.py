from flask import Flask, request, jsonify
import requests
import hashlib

app = Flask(__name__)

@app.route('/v1/proxy-check-email/', methods=['GET'])
def proxy_check_email_query():
    email = request.args.get('email')

    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        response = requests.get(f'https://api.xposedornot.com/v1/check-email/{email}')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/v1/proxy-breach-analytics/', methods=['GET'])
def proxy_breach_analytics():
    email = request.args.get('email')

    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        response = requests.get(f'https://api.xposedornot.com/v1/breach-analytics?email={email}')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/v1/proxy-password-check/<password_hash>', methods=['GET'])
def proxy_password_check(password_hash):
    try:
        response = requests.get(f'https://passwords.xposedornot.com/v1/pass/anon/{password_hash}')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/v1/proxy-all-breaches/', methods=['GET'])
def proxy_all_breaches():
    try:
        response = requests.get('https://api.xposedornot.com/v1/breaches')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/v1/proxy-breaches-by-domain/', methods=['GET'])
def proxy_breaches_by_domain():
    domain = request.args.get('domain')

    if not domain:
        return jsonify({"error": "Domain parameter is required"}), 400

    try:
        response = requests.get(f'https://api.xposedornot.com/v1/breaches?domain={domain}')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/v1/proxy-domain-breaches/', methods=['GET'])
def proxy_domain_breaches():
    try:
        response = requests.get('https://api.xposedornot.com/v1/domain-breaches/')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
