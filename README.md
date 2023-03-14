# Pandoc Convert API

Not support to pdf

## Usage

Start http server
```
docker run --rm -p 5000:5000 chanmo/pandoc
```

convert to html, use httpie
```
http -f POST :5000/convert/html file@~/demo.docx
```

## APIs

```
/convert/{format}
```
