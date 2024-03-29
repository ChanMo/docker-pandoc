# Pandoc Convert API

Notice: There is no support for converting to PDF format.

For more tools to help you manage and use your documents, visit [Awesome Document](https://www.chanmo.me/awesome_document.html)

## Usage

Start the API server
```
docker run --rm -p 5000:5000 chanmo/pandoc
```

Convert the DOCX file to HTML format, by httpie
```
http -f POST :5000/convert/html file@~/demo.docx
```

Result:
```
{
    "media": [],
    "output": "/uploads/c2528467-3050-4d20-b5be-192fc273c86e.html",
    "success": true
}
```

Then, you can download the HTML file from the output value.

If you want the API to return the binary data directly, you can add the `download=true`:
```
http -f POST :5000/convert/html?download=true file@~/demo.docx -o demo.html
```

## APIs

```
/convert/{format}
```

The formats that is supported:
* xml
* html
* markdown
* org
* epub

Visit https://pandoc.org/, and get more help.
