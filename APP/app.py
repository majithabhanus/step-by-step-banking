from flask import Flask, jsonify

app = Flask(__name__)

accounts = [
    {
        "id": 101,
        "customer": "John",
        "account_type": "Savings",
        "balance": 50000
    },
    {
        "id": 102,
        "customer": "Alice",
        "account_type": "Current",
        "balance": 75000
    }
]


@app.route("/")
def home():
    return "Banking Account Service is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/accounts")
def get_accounts():
    return jsonify(accounts)


@app.route("/accounts/<int:account_id>")
def get_account(account_id):

    for account in accounts:
        if account["id"] == account_id:
            return jsonify(account)

    return jsonify({
        "error": "Account not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)