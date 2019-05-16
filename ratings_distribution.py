from itertools import islice
import matplotlib.pyplot as plt
ratings = []
with open('ratings.csv') as csv:
    for line in islice(csv, 1, None):  # skip the first line
        line = line.strip().split(',')
        print(line)
        rating = float(line[2])
        # ratings.append(rating)
# ratings = sorted(ratings)
# plt.hist(ratings, rwidth=0.9, color='#607c8e')
# plt.xlim((0.5, 5))
# plt.xlabel('Ratings')
# plt.ylabel('Numbers')
# plt.title("Rating distribution")
# plt.show()
# print("run over!")
#
# movie_rate_number = []
# with open('ratings.csv') as csv:
#     for line in islice(csv, 1, None):  # skip the first line
#         line = line.strip().split(',')
#         movie_id = int(line[1])
#         movie_rate_number[movie_id] += 1
#


