from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from fasttext import load_model

app = FastAPI()
AUTH_KEY = "secret"

model = load_model("./lid.176.ftz")
LANGS = ("ja", "en", "es")


def predict_lang(t: str):
    preds = model.predict(t)
    pred_langs = [p.replace("__label__", "") for p in preds[0]]
    for lang in pred_langs:
        if lang in LANGS:
            return lang
    return LANGS[0]


class Req(BaseModel):
    text: str


@app.post("/identify")
def identify(item: Req, Authorization: str = Header(None)):

    if AUTH_KEY != Authorization:
        raise HTTPException(status_code=401, detail="wrong authorization key")

    return {"lang": predict_lang(item.text)}
