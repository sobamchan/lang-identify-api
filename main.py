import os
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Header, HTTPException
from fasttext import load_model

load_dotenv()

app = FastAPI()
AUTH_KEY = os.getenv("SECRET")

model = load_model("./lid.176.ftz")
LANGS = ("ja", "en", "es")


def predict_lang(t: str):
    preds = model.predict(t)
    pred_langs = [p.replace("__label__", "") for p in preds[0]]
    for lang in pred_langs:
        if lang in LANGS:
            return lang
    return LANGS[0]


@app.post("/identify")
def identify(
        text: str = Body(..., embed=True), Authorization: str = Header(None)
        ):

    if Authorization != AUTH_KEY:
        raise HTTPException(status_code=401, detail="wrong authorization key")

    return {"lang": predict_lang(text)}
