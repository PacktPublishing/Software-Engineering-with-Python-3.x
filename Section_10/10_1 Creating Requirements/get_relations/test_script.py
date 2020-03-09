from get_relations import EmailRelations

data_dict = [{'From': 'John', 'To': 'May'},
			{'From': 'Michael', 'To': 'Jim'},
			{'From': 'Pamela', 'To': 'Cole'},
			{'From': 'Darry', 'To': 'Carry'},
			{'From': 'John', 'To': 'Pamela'},
			{'From': 'May', 'To': 'John'},
			{'From': 'Michael', 'To': 'May'},
			{'From': 'Pamela', 'To': 'May'}]

email_rels_obj = EmailRelations(data_dict,
								max_rep=15,
								csv_fname='mails.csv',
								dot_fname='processed.dot',
								png_fname='relations.png')

email_rels_obj.create_relations_image()