from flask import Flask, jsonify, request


app = Flask(__name__)

#init board
game = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]


@app.route("/game", methods=["GET"])
def get_game():
    return jsonify({'game' : game}) # it is actually that simple !!!

@app.route('/move', methods=['POST'])
def post_move():
    post_json = request.get_json()
    new_obj = json_to_game_object(post_json)
    #will have some object that is player, old tile and new tile

    #we check the logic of that move here

    #if we like it change the board accordingly



    board.append(new_quark)
    return jsonify({'board' : board})

# @app.route("/")
# def hello():
#     return jsonify({'message' : 'Hello, World!'})

if __name__ == "__main__":
    app.run()