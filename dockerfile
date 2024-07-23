FROM python:3.8.10-alpine as builder
RUN apk add --no-cache linux-headers gcc musl-dev zlib-dev
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pyinstaller /usr/src/app/main.py --clean --onefile -y

FROM alpine:latest
COPY --from=builder /usr/src/app/dist/main /usr/bin/deployjenkins
RUN chmod +x /usr/bin/deployjenkins
CMD ["/usr/bin/deployjenkins"]
