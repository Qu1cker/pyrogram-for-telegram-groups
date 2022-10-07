import postgres

row = postgres.question_get(1)
# question = row[1]
# answer = row[2]
r = row[0]

print(r[3])
