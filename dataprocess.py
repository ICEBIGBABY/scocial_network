from itertools import islice
with open('ratings.csv') as csv:
    movie_id = 0
    flag = 0
    for line in islice(csv, 1, None):  # skip the first line
        line = line.strip().split(',')
        if line[1] == str(movie_id):
            f = open('movies/movie_'+str(movie_id)+'.txt', 'a')
            if flag == 0:
                f.write(str(movie_id)+':'+'\n')
                flag = 1
            f.write(line[0] + ',' + line[2] + ',' + line[3] + '\n')
        else:
            movie_id += 1
            flag = 0

print("run over!")
