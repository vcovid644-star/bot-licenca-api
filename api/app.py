from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {}

@app.route("/")
def home():
    return "API de Licenças Online 🚀"

@app.route("/check", methods=["POST"])
def check_license():
    data = request.json
    guild_id = str(data.get("guild_id"))

    licenca = licenses.get(guild_id)
    if not licenca:
        return jsonify({"status": "invalid"})

    return jsonify({
        "status": "valid",
        "plano": licenca["plano"],
        "expira_em": licenca["expira_em"]
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
