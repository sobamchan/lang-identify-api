```bash
cp .env.sample .env
uvicorn main:app --reload --port 8000
```

then,

```bash
curl --location --request POST 'http://127.0.0.1:8000/identify' \
--header 'Authorization: secret' \
--header 'Content-Type: application/json' \
--data-raw '{
	"text": "hello"
}'
```
