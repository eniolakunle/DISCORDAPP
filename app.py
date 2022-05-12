from flask import Flask, render_template, request, escape
from flask import redirect, url_for, make_response
from discord_text_parser import DiscordParser, ParseException
from td_client import (
    TDClient,
    TDCreds,
    TokenException,
    ACCOUNT_ID,
    CONSUMER_KEY,
    REFRESH_TOKEN,
)
import logging
import datetime

app = Flask(__name__)
parser = DiscordParser()
TODAY = datetime.date.today()
logging.basicConfig(
    filename=f"logs/mainapp_{TODAY}.log",
    encoding="utf-8",
    level=logging.INFO,
)
CREDS = None


# @app.route("/")
# def creds():
#     response = request.args.get("response", "")
#     return render_template("creds.html", response=response)


@app.route("/")
def index():
    if CREDS or all([ACCOUNT_ID, CONSUMER_KEY, REFRESH_TOKEN]):
        return render_template("index.html")
    else:
        response = request.args.get("response", "")
        return render_template("creds.html", response=response)


@app.route("/creds", methods=["POST"])
def _check_creds():
    try:
        if request.method == "POST":
            account_id = int(request.form.get("account_id"))
            consumer_key = request.form.get("consumer_key")
            refresh_token = request.form.get("refresh_token")
            try:
                creds = TDCreds(account_id, consumer_key, refresh_token)
                global CREDS
                CREDS = creds
                url = url_for("index")

            except TokenException as e:
                url = url_for("index", response=f"{e}")
    except Exception as e:
        url = url_for("index", response=f"Invalid entry.")

    return redirect(url)


@app.route("/results")
def return_results():
    discord_text = request.args.get("discord_text")
    response = request.args.get("response")
    parsed_text = request.args.get("parsed_text")
    return make_response(
        render_template(
            "index.html",
            input_text=discord_text,
            parsed_text=parsed_text,
            response=response,
        ),
        200,
    )


@app.route("/invalid")
def invalid_results():
    discord_text = request.args.get("discord_text")
    response = request.args.get("response")
    return make_response(
        render_template(
            "index.html",
            input_text=discord_text,
            response=response,
        ),
        400,
    )


@app.route("/submit")
def get_discord_text():
    discord_text = str(escape(request.args.get("discord_text", "")))

    try:
        parsed_text, amount = _get_parsed_text_and_amount(discord_text)
    except ParseException as e:
        return redirect(
            url_for(
                "invalid_results",
                discord_text=discord_text,
                response=f"{e}",
            )
        )
    url = _return_url(parsed_text, amount, discord_text)
    return redirect(url)


def _return_url(parsed_text: str, amount: int, discord_text):
    if parsed_text:
        try:
            response = _place_order(parsed_text, amount)
            url = url_for(
                "return_results",
                discord_text=discord_text,
                parsed_text=parsed_text,
                response=response,
            )
        except TokenException:
            url = url_for(
                "invalid_results",
                discord_text=discord_text,
                response="Unable to connect to TD, please check credentials.",
            )

        except Exception as e:
            url = url_for(
                "invalid_results",
                discord_text=discord_text,
                response=f"{e}",
            )

    else:
        url = url_for(
            "invalid_results",
            discord_text=discord_text,
            response="Invalid Symbol",
        )
    return url


def _get_parsed_text_and_amount(discord_text: str):
    parsed_text, amount = (
        parser.parse(discord_text) if discord_text.strip() else (None, None)
    )

    logging.info(f"PARSED: {parsed_text}")
    logging.info(f"AMOUNT: {amount}")
    return parsed_text, amount


def _place_order(parsed_text: str, amount: int):
    client = TDClient(CREDS)
    response = client.place_order(parsed_text, amount)
    logging.info(f"RESPONSE: {response}")
    return response


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8080, debug=True)
    app.run(host="0.0.0.0", debug=True)
