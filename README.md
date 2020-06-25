# Python Selenium Flask Example

In the next example, we create a test case with `pytest` and Selenium for a Flask web application. We test for a response from an HTML form.

  app.py
  ├───static
  │       greet.html
  ├───templates
  │       index.html
  └───tests
          web_test.py


To run:

```bash
set FLASK_APP=app.py
flask run
```

and in a separate terminal, run

```bash
pytest
```


#### Resources:
<a href = 'http://zetcode.com/python/selenium/'> http://zetcode.com/python/selenium/ </a>
