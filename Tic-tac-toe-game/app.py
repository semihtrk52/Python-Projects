from flask import Flask, render_template, request, session
import os
import binascii
import random

app = Flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24)).decode()  # Güvenli bir anahtar oluşturur

@app.route("/", methods=["GET", "POST"])
def index():
    if 'game_board' not in session:
        session['game_board'] = [["", "", ""], ["", "", ""], ["", "", ""]]
        session['turn_sayac'] = 0
        session['winner'] = None
        session["number_board"] = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # 0-8 aralığında indeksler

    if request.method == "POST":
        if request.form.get("new_game"):
            session['game_board'] = [["", "", ""], ["", "", ""], ["", "", ""]]
            session['turn_sayac'] = 0
            session['winner'] = None
            session["number_board"] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            return render_template("index.html", game_board=session['game_board'])

        number_list = session["number_board"]
        turn_sayac = session['turn_sayac']
        turn = "X" if turn_sayac % 2 == 0 else "O"

        if turn == "X":
            num = int(request.form.get("value")) - 1
            number_list.remove(num)
        else:
            num = random.choice(number_list)
            number_list.remove(num)

        session["number_board"] = number_list

        game_board = session['game_board']
        row, col = divmod(num, 3)


        if game_board[row][col] not in ['X', 'O']:
            game_board[row][col] = turn
            session['game_board'] = game_board

            if (
                (game_board[0][0] == game_board[0][1] == game_board[0][2] != '') or
                (game_board[1][0] == game_board[1][1] == game_board[1][2] != '') or
                (game_board[2][0] == game_board[2][1] == game_board[2][2] != '') or
                (game_board[0][0] == game_board[1][0] == game_board[2][0] != '') or
                (game_board[0][1] == game_board[1][1] == game_board[2][1] != '') or
                (game_board[0][2] == game_board[1][2] == game_board[2][2] != '') or
                (game_board[0][0] == game_board[1][1] == game_board[2][2] != '') or
                (game_board[2][0] == game_board[1][1] == game_board[0][2] != '')
            ):
                winner = turn
                session['winner'] = winner
                if session['winner'] == "O":
                    return render_template("loser.html")
                return render_template("winner.html", winner=winner)

            # Beraberlik kontrolü
            if all(cell in ['X', 'O'] for row in game_board for cell in row):
                session['winner'] = 'Draw'
                return render_template("draw.html")

            session['turn_sayac'] += 1

        return render_template("index.html", game_board=game_board)

    return render_template("index.html", game_board=session['game_board'])

if __name__ == "__main__":
    app.run(debug=True)
