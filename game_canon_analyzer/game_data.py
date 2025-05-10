composers = [
	{"ID":  1, "name": "Mozart, Wolfgang Amadeus",
		"birth_year": 1756, "death_year": 1791,
		"nation": "AUT", "gender": "m"},
	{"ID":  2, "name": "Beethoven, Ludwig van",
		"birth_year": 1770, "death_year": 1827,
		"nation": "DEU", "gender": "m"},
	{"ID":  3, "name": "Wagner, Richard",
		"birth_year": 1813, "death_year": 1883,
		"nation": "DEU", "gender": "m"},
	{"ID":  4, "name": "Kreutzer, Rodolphe",
		"birth_year": 1766, "death_year": 1831,
		"nation": "FRA", "gender": "m"},
	{"ID":  5, "name": "Weber, Carl Maria von",
		"birth_year": 1786, "death_year": 1826,
		"nation": "DEU", "gender": "m"},
	{"ID":  6, "name": "Bach, Johann Sebastian",
		"birth_year": 1685, "death_year": 1750,
		"nation": "DEU", "gender": "m"},
	{"ID":  7, "name": "Meyerbeer, Jacob",
		"birth_year": 1791, "death_year": 1864,
		"nation": "DEU", "gender": "m"},
	{"ID":  8, "name": "Mendelssohn Bartholdy, Felix",
		"birth_year": 1809, "death_year": 1847,
		"nation": "DEU", "gender": "m"},
	{"ID":  9, "name": "Haydn, Joseph",
		"birth_year": 1732, "death_year": 1809,
		"nation": "AUT", "gender": "m"},
	{"ID": 10, "name": "Händel, Georg Friedrich",
		"birth_year": 1685, "death_year": 1759,
		"nation": "DEU", "gender": "m"},
	{"ID": 11, "name": "Lortzing, Albert",
		"birth_year": 1801, "death_year": 1851,
		"nation": "DEU", "gender": "m"},
	{"ID": 12, "name": "Silcher, Friedrich",
		"birth_year": 1789, "death_year": 1860,
		"nation": "DEU", "gender": "m"},
	{"ID": 13, "name": "Verdi, Giuseppe",
		"birth_year": 1813, "death_year": 1901,
		"nation": "ITA", "gender": "m"},
	{"ID": 14, "name": "Schubert, Franz",
		"birth_year": 1797, "death_year": 1828,
		"nation": "AUT", "gender": "m"},
	{"ID": 15, "name": "Liszt, Franz",
		"birth_year": 1811, "death_year": 1886,
		"nation": "HUN", "gender": "m"},
	{"ID": 16, "name": "Schumann, Robert",
		"birth_year": 1810, "death_year": 1856,
		"nation": "DEU", "gender": "m"},
	{"ID": 17, "name": "Gluck, Christoph Willibald",
		"birth_year": 1714, "death_year": 1787,
		"nation": "DEU", "gender": "m"},
	{"ID": 18, "name": "Rossini, Gioacchino",
		"birth_year": 1792, "death_year": 1868,
		"nation": "ITA", "gender": "m"},
	{"ID": 19, "name": "Gounod, Charles",
		"birth_year": 1818, "death_year": 1893,
		"nation": "FRA", "gender": "m"},
	{"ID": 20, "name": "Rubinstein, Anton",
		"birth_year": 1829, "death_year": 1894,
		"nation": "RUS", "gender": "m"},
	{"ID": 21, "name": "Brahms, Johannes",
	 "birth_year": 1833, "death_year": 1897,
	 "nation": "DEU", "gender": "m"},
	{"ID": 22, "name": "Bruckner, Anton",
	 "birth_year": 1824, "death_year": 1896,
	 "nation": "AUT", "gender": "m"},
	{"ID": 23, "name": "Strauss, Richard",
	 "birth_year": 1864, "death_year": 1949,
	 "nation": "DEU", "gender": "m"}
]

games = [
	{"ident": "Haußer", "contents": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "game_date": None},
	{"ident": "N/A", "contents": [13, 9, 14, 8, 1, 11, 3, 6, 15, 5, 16, 2], "game_date": None},
	{"ident": "The Great Composers", "contents": [6, 10, 17, 9, 1, 2, 5, 7, 18, 14, 16, 15, 13, 3, 8, 19, 20], "game_date": None}
	# {"ident": "Smigelski", "contents": [6, 10, 9, 1, 2, 14, 16, 21, 3, 22, 23], "game_date": None}
]


def sort_by_name(composers):
	return sorted(composers, key=lambda composer: composer["name"])

def sort_by_birth(composers):
	return sorted(composers, key=lambda composer: composer["birth_year"])


if __name__ == "__main__":
	print("DATA CHECK: COMPOSERS\n")
	for index, composer in enumerate(sort_by_name(composers)):
		print(f"{index + 1}. {composer['name']} ({composer['birth_year']}-{composer['death_year']}): {composer['nation']}, {composer['gender']}")

	composer_dict = {composer["ID"]: composer for composer in composers}

	print("\nDATA CHECK: GAMES\n")
	for index, game in enumerate(games):
		print(f"{index + 1}. {game['ident']}:")
		in_game = sorted(game["contents"])
		for comp_index, comp_id in enumerate(sorted(game["contents"])):
			comp = composer_dict[comp_id]
			print(f"-> ID {comp_id}: {comp['name']} ({comp['birth_year']}-{comp['death_year']})")
		print()

	print("DATA CHECK COMPLETE.")