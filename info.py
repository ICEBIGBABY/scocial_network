# -*- coding: utf-8 -*

from collections import Counter
import numpy as np
from itertools import islice
import matplotlib.pyplot as plt
import csv


def load_file(filename):
    count = -1

    with open(filename) as f:
        for line in islice(f, 1, None):
            count+=1
            if count%100==0:
                print count
            split_line = line.strip().split(",")
            movie_id = int(split_line[1])
            user_id = int(split_line[0])
            rating = float(split_line[2])
            timestamp = split_line[3]

            add_movie(movie_id)
            add_rating(movie_id, user_id, rating, timestamp)
    # ratings[movie_id] = np.mean(ratings[movie_id])
    # ratings[movie_id] = float(sum(ratings[movie_id])/len(ratings[movie_id]))

def add_movie(movie_id):
    if movie_id not in ratings:
        ratings[movie_id] = []


def add_rating(movie_id, user_id, rating, timestamp):
    movie_counter[movie_id] += 1
    user_counter[user_id] += 1
    rating_counter[rating] += 1
    ratings[movie_id].append(rating)

def draw_distribution(counter, title, xlabel, ylabel):
    num_rating = counter.values()
    degree_counter = Counter(num_rating)
    rating_list = list(degree_counter)
    num_list = degree_counter.values()
    plt.loglog(rating_list, num_list, 'o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


if __name__== '__main__':
    # file = r'ml-20m/ratings.csv'
    file = r'ratings.csv'
    movie_counter = Counter()  #movie_id:sum_rating
    user_counter = Counter()   #user_id:sum_rating
    rating_counter = Counter() #rating:sum_rating
    ratings = {}

    load_file(file)

    # print len(user_counter)   #610
    # print len(movie_counter)  #9724
    # print sum(rating_counter.values())   #100836

    # plt.figure(1)
    # draw_distribution(user_counter, "Log-log plot of ratings each user has made", "Ratings a user has made", "Users")
    # plt.figure(2)
    # draw_distribution(movie_counter, "Log-log plot of ratings each movie has received", "Ratings a movie has received", "Movies")
    # plt.figure(3)
    # items = sorted(rating_counter.items(),key=lambda x:x[0])
    # rat = []
    # r_num = []
    # for item in items:
    #     rat.append(item[0])
    #     r_num.append(item[1])
    # plt.bar(rat, r_num, width=0.3)
    # plt.xlabel("Rating")
    # plt.ylabel("The number of ratings")
    # plt.title("Distribution of user ratings for movies")
    # # plt.legend()
    # plt.show()





