## **Task 1: Environment Setup**

I previously installed flask. Here's me setting up the git repository:

![[Images/Pasted image 20240115130855.png]]

## **Task 2: Create a Flask Application**

I used nano in wsl to whip up a basic Flask application. I followed the instructions on the Flask website. I tested the app and it worked.

![[Images/Pasted image 20240115132131.png]]
## **Task 3: Create a Static HTML Page**

I'm a bit rusty, but I made a decent form after some time messing with css

![[Images/Pasted image 20240115141505.png]]

I'm using a div and a form for layout.

```html
    <body>
        <div class="center">
            <label>Input something!</label>
            <form>
                <input type="text"/>
                <button>Input</button>
            </form>
        </div>
    </body>
```

## Task 4: Create Flask Routes

I changed the flask code to render the index.html page. It worked, but didn't render the css

![[Images/Pasted image 20240115152344.png]]

I looked it up, and apparently you need to put css files in a folder called "static" and use this format to link to it in the html document:

```CSS
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">`
```

It works now.

## **Task 5: Handle Form Submission**

I wrote the following method which takes the result from the form and routes to a new page.

```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        input_text = request.form['input_text']
        return render_template('result.html', input_text=input_text)
    return render_template('index.html')
```

I changed the form in index.html to support this functionality

```html
<body>
    <div class="center">
        <label>Input something!</label>
        <form action="/submit" method="post">
            <input type="text" name="input_text"/>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
```

It works:

![[Images/Pasted image 20240115164625.png]]

![[Images/Pasted image 20240115164637.png]]

