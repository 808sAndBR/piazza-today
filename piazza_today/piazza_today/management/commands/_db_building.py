all_names =[('Alaina' , 'Murphy'),
('David' , 'Tilley'),
('Jessica' , 'Gilmartin'),
('Matthew' , 'Ewer'),
('Michael' , 'Lam'),
('Rhia' , 'Jovellanos'),
('Tiffany' , 'Zhu'),
('Renars' , 'Galis'),
('Akhila' , 'Iruku'),
('Brandon' , 'Fennell'),
('John' , 'Knight'),
('Pooja' , 'Sankar'),
('Sunthar' , 'Premakumar'),
('Tony' , 'Luckett'),
('Tamara' , 'Jordan'),
('Tim' , 'Inman'),
('Janis' , 'Galis'),
('Melissa' , 'Sobel'),
('Matt' , 'Birnbaum'),
('Johann' , 'John'),
('Glenda' , 'Mosley'),
('Nick' , 'Deierlein'),
('Tim' , 'Inman'),
('Will' , 'Gahagan'),
('Jason' , 'Ford'),
('Victoria' , 'Lewkowitz'),
('Zach' , 'Gottlieb')]

for name in all_names:
	first_name = name[0]
	last_name = name[1]
	email = first_name.lower()+'@piazza.com'
	username = email
	new_user = User.objects.create_user(username, email, 'Kanye101')
	new_user.is_active = False
	new_user.first_name = first_name
	new_user.last_name = last_name
	new_user.save()