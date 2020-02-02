name = input("Input your name: ")
birthplace = input("Input your birthplace: ")
address = input('Input your current address: ')
contact = input('Input your contact info: ')
school = input('Input your school: ')
degree = input('Input your major/degree: ')
specialization = input('Input your specialization: ')
school_city = input('Input the city of your school: ')
school_start = input('Input the month/year that you graduated: ')
gpa = input('Input your GPA (out of 4.0): ')
html = f"""<!DOCTYPE html>
<html>
<head>
	<title>my CV</title>
</head>
<body>

	<div id="top">
		<h1>{name}</h1>
	</div>

	<h5 id="birthplace">
		Birthplace: {birthplace}
	</h5>
	
	<h5 id="address">
	Current Address: {address}
	</h5>

	<h5 id="contact">
		{contact}
	</h5>


	<h2 class="heading">Education</h2>
	<div>
		<div class="left">
			<p id="Organizations">
				<strong>{school}</strong>
			</p>

			<p id="Positions">
				<em>{degree}</em>
			</p>

			<ul id="Descriptions">
				<li>{specialization}</li>
			</ul>
		</div>

		<div class="right">
			{school_city} <br> 
			{school_start} <br> 
			GPA: {gpa} / 4.00
		</div>
	</div>

	<div class="clear"></div>

</body></html>"""
print(html)
file = open("mycv.html", 'w')
file.write(html) 
file.close()