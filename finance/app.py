import os

import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT * FROM purchases WHERE user_id = ?", session["user_id"])
    for stock in stocks:
        stock_data = lookup(stock['symbol'])
        if stock_data is not None:
            stock["name"] = stock_data["name"]
            stock["cprice"] = stock_data["price"]
    cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
    cash = cash[0]["cash"]
    total = cash
    for stock in stocks:
        total += stock["cprice"] * stock["shares"]
        stock["price"] = usd(stock["price"])
    username = db.execute("SELECT username FROM users WHERE id=?", session["user_id"])[0]["username"]
    return render_template("index.html", stocks=stocks, cash=usd(cash), total=usd(total), username=username)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    elif request.method == "POST":
        try:
            if request.form.get("symbol") == "":
                return apology("Input a stock symbol")
            stock = lookup(request.form.get("symbol"))
            if stock is None:
                return apology("The stock does not exist")
            if int(request.form.get("shares")) < 0:
                return apology("You can't buy a negative stock")
            shares = int(request.form.get("shares"))
            cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
            cash = cash[0]["cash"]
            cash -= ((lookup(request.form.get("symbol"))["price"]) * shares)
            old_stocks = db.execute("SELECT id FROM purchases WHERE user_id=? AND symbol=?",
                                    session["user_id"], request.form.get("symbol"))
            if old_stocks == []:
                db.execute("INSERT INTO purchases(user_id, symbol, date, shares, price) VALUES (?,?,?,?,?)",
                           session["user_id"], stock["symbol"], get_date(), shares, stock["price"])
            else:
                old_stocks = old_stocks[0]["id"]
                new_shares = db.execute("SELECT shares FROM purchases WHERE id=? AND symbol=?",
                                        session["user_id"], request.form.get("symbol"))
                new_shares = new_shares[0]["shares"]
                new_shares += shares
                db.execute("UPDATE purchases SET shares=? WHERE id=?", new_shares, old_stocks)
            db.execute("UPDATE users SET cash=? WHERE id=?", cash, session["user_id"])
            db.execute("INSERT INTO transactions (date, symbol, user_id, action, shares) VALUES (?,?,?,?,?)",
                       get_date(), request.form.get("symbol"), session["user_id"], "buy", shares)
            return redirect("/")
        except:
            return apology("Oops, something went wrong!!!")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    histr = db.execute("SELECT * FROM transactions WHERE user_id=?", session["user_id"])
    for transaction in histr:
        transaction["name"] = lookup(transaction["symbol"])["name"]
    return render_template("history.html", history=histr)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if quote is None:
            return apology("Quote does not exist")
        return render_template("quoted.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        if request.form.get("username") == "":
            return apology("You have to input a name")
        if request.form.get("password") == "":
            return apology("You have to input a password")
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and confirmation do not match")
        new_user = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }
        user_exists = db.execute("SELECT id FROM users WHERE username=?", [new_user["username"]])
        if user_exists:
            return apology("The username already exists")
        db.execute("INSERT INTO users(username, hash) VALUES (?,?)", new_user["username"], new_user["password"])
        session["user_id"] = (db.execute("SELECT id FROM users WHERE username=?", new_user["username"]))[0]["id"]
        return redirect("/quote")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols_data = db.execute("SELECT symbol FROM purchases WHERE user_id=?", session["user_id"])
        symbols = []
        for symbol in symbols_data:
            symbols.append(symbol["symbol"])
        return render_template("sell.html", symbols=symbols)
    elif request.method == "POST":
        shares = int(request.form.get("shares"))
        symbol = request.form.get("symbol")
        if shares is None:
            return apology("Input a number of shares")
        if symbol is None:
            return apology("Input a symbol")
        if lookup(symbol) is None:
            return apology("Stock does not exist")
        if shares < 0:
            return apology("cannot sell a negative number of shares")
        new_shares = db.execute("SELECT shares FROM purchases WHERE user_id=? AND symbol=?", session["user_id"], symbol)
        new_shares = new_shares[0]["shares"]
        new_shares -= shares
        cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
        cash = cash[0]["cash"]
        cash += ((lookup(symbol)["price"]) * shares)
        if new_shares < 0:
            return apology("You don't have enough shares")
        elif new_shares == 0:
            db.execute("DELETE FROM purchases WHERE symbol=? AND user_id=?", symbol, session["user_id"])
        else:
            db.execute("UPDATE purchases SET shares=? WHERE user_id=?", new_shares, session["user_id"])
        db.execute("UPDATE users SET cash=? WHERE id=?", cash, session["user_id"])
        db.execute("INSERT INTO transactions (date, symbol, user_id, action, shares) VALUES (?,?,?,?,?)",
                   get_date(), symbol, session["user_id"], "sell", shares)
    return redirect("/")


@app.route("/cash", methods=["POST"])
def cash():
    c_cash = float(db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])[0]["cash"])
    if float(request.form.get("cash")) < 0:
        return apology("You cannot add negative cash")
    elif float(request.form.get("cash")) == 0:
        return apology("You cannot add zero cash")
    c_cash += float(request.form.get("cash"))
    db.execute("UPDATE users SET cash=? WHERE id=?", c_cash, session["user_id"])
    return redirect("/")


def get_date():
    time = datetime.datetime.now()
    return time.strftime("%x")