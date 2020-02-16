def make_pizza(size, *toppings):
    html = f"""
            <html>
                <body>
                    <h1>Making a {size}-inch pizza with toppings:</h1>
                </body>
            </html>
            """
    for topping in toppings:
        html += f"""<p>{topping}</p>"""

    return html

