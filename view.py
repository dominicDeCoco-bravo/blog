from app import app
from flask import render_template
import sqlite3
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify

@app.route("/list")
def index():
    conn = sqlite3.connect("comm.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists comments(id integer primary key asc, comment text)")
    cursor.execute("SELECT * FROM comments")
    comments = cursor.fetchall()
    return jsonify([{'id':id_,'text': text} for (id_, text) in comments])
@app.route("/add", methods=['POST'])
def add_comm():
    text=request.json['text']
    conn = sqlite3.connect("comm.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comments(comment) VALUES(?)",[text])
    conn.commit()
    return jsonify({})
@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_comm(id):
    conn = sqlite3.connect("comm.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM comments WHERE id =?",[id])
    conn.commit()
    return jsonify({})
