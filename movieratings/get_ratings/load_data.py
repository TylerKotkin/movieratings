def load_ml_data():
    import csv
    import json

    users = []

    with open('../ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'get_ratings.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)

    with open('users.json', 'w') as f:
        f.write(json.dumps(users))

    # print(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))

    ratings = []

    with open('../ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating'.split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'stars': row['Rating'],
                    'rater': row['UserID'],
                    'movie': row['MovieID']
                },
                'model': 'get_ratings.Rating',
            }

            ratings.append(rating)


    with open('fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))


    movies = []

    with open('../ml-1m/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title']
                },
                'model': 'get_ratings.Movie',
                'pk': row['MovieID']
            }

            movies.append(movie)

    with open('movies.json', 'w') as f:
        f.write(json.dumps(movies))

load_ml_data()
