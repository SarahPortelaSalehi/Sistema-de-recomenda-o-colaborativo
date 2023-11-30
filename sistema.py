def minkowski(rating1, rating2, r):
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key] - rating2[key]), r)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1/r)
    else:
        return 0

def computeKNearestNeighbors(new_user_ratings, users, k):
    distances = []

    for username, existing_ratings in users.items():
        distance = minkowski(new_user_ratings, existing_ratings, 2)
        distances.append((distance, username))

    distances.sort()
    return distances[:k]

def recommendK(new_user_ratings, users, k, num_recommendations):
    nearest_neighbors = computeKNearestNeighbors(new_user_ratings, users, k)
    recommendations = []

    for neighbor in nearest_neighbors:
        neighbor_name = neighbor[1]
        neighbor_ratings = users[neighbor_name]

        for movie, rating in neighbor_ratings.items():
            if movie not in new_user_ratings:
                recommendations.append((movie, rating))

    recommendations.sort(key=lambda movieTuple: movieTuple[1], reverse=True)
    return recommendations[:num_recommendations]