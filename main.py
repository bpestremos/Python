from flask import Flask, request, jsonify
import sql
import sqlConn

app = Flask(__name__)

@app.route("/get_user/Employees")
def get_user():
    json = sql.READ(sql.conn)
    return jsonify(json), 200



@app.route("/post/Employees", methods=["POST"])
def post_user():
    sql.CREATE(sql.conn)
    return ("test API POST to Employees table")


if __name__ == "__main__":
    app.run(debug=True)




sql.conn.close()
