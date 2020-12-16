from flask import Flask, jsonify, request


app = Flask(__name__)

#init board
board = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]


@app.route("/board", methods=["GET"])
def get_board():
    return jsonify({'board' : board})

@app.route('/board', methods=['POST'])
def propose_board():
    new_quark = request.get_json()
    board.append(new_quark)
    return jsonify({'board' : board})

@app.route("/")
def hello():
    return jsonify({'message' : 'Hello, World!'})

if __name__ == "__main__":
    app.run()