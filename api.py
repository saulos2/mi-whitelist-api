from flask import Flask, request, jsonify
import os # Necesario para el puerto en Vercel

app = Flask(__name__)

# --- Tu Fuente de Datos Whitelist (¡Reemplazar con DB en el futuro!) ---
WHITELIST_DATA = {
    "Player1": {"discord": "Player1Discord#1111", "whitelisted": True},
    "Player2": {"discord": "User2#2222", "whitelisted": True},
    "NotWhitelisted": {"discord": "Banned#9999", "whitelisted": False},
    # Agrega aquí los nombres de usuario de Roblox y su estado
    "TuUsuarioRoblox": {"discord": "TuDiscord#1234", "whitelisted": True}
}
# -------------------------------------------------------------------

# IMPORTANTE: En Vercel, las rutas suelen ir bajo /api/
@app.route('/api/check', methods=['GET'])
def check_whitelist():
    roblox_username = request.args.get('roblox')

    if not roblox_username:
        return jsonify({"error": "Falta el parámetro 'roblox'"}), 400

    user_data = WHITELIST_DATA.get(roblox_username)

    if user_data:
        response_data = {
            "username": roblox_username,
            "discord": user_data.get("discord"),
            "whitelisted": user_data.get("whitelisted", False)
        }
        return jsonify(response_data), 200
    else:
        response_data = {
            "username": roblox_username,
            "discord": None,
            "whitelisted": False
        }
        return jsonify(response_data), 200

# Ruta raíz simple para verificar que funciona
@app.route('/api', methods=['GET'])
@app.route('/', methods=['GET']) # También la raíz por si acaso
def index():
    return "API Whitelist funcionando!"

# --- No necesitas app.run() aquí, Vercel se encarga ---
# if __name__ == '__main__':
#    app.run(debug=True) # Esto es solo para pruebas locales