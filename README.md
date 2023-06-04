# Bayesian-Anime-Recommender
The Anime Recommender Machine Learning Model v0 is a recommendation system that suggests anime based on user preferences and ratings. It utilizes the Naive Bayes algorithm to compute the probability of each anime being recommended.

Anime Recommender using Naive Bayes Model
By: Raymond Llata

# Training Data:
The data used to train this model was sourced from Kaggle. The data was provided in the form of two CSV files: Anime.csv, which contained an Anime ID, Name, Genre, Type of Show, Episode Count, Rating and Popularity attribute for over 17,000 Anime, and Rating.csv which provided a user-specific rating for every anime, spanning over 64,000 Users. In total, this was 110 Megabytes of Data. 

Link:  https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

To reduce the computation time for this project, I had to reduce the scope of recommendations. For input animes I looked at a users rating for the 5 most popular anime (Death Note, Attack On Titan, Sword Art Online, Angel Beats, and Mirai Nikki). For the output anime, I picked 5 distinct shows that are unlikely to share a huge viewer demographic  Steins;Gate, Fullmetal Alchemist, Toradora, No Game No Life, and Clannad) based on personal knowledge . However, the attributes of the data from Kaggle were not well-suited for my project and, as a result, I spent a significant portion of time cleaning data. 

# Data Cleaning:
The data cleaning process begins with the writeCSV() function. This function utilizes two helper functions, userToFavGenreDict() and dictOfUserAnime(), to generate user statistics and a dictionary of user-anime ratings, respectively. The generated data is then written to a new CSV file called "newAnime.csv".

Within the writeCSV() function, variables are initialized for each key anime, such as Death Note, Attack On Titan, Sword Art Online, Angel Beats, and Mirai Nikki. Additionally, there are variables for other anime like Steins;Gate, Fullmetal Alchemist, Toradora, No Game No Life, and Clannad.

# Data Verification:
The data verification process is performed by the testCSV() function, which reads the "newAnime.csv" file. The function checks for the presence of key anime ratings for each user. To facilitate this verification, boolean variables are initialized as false for each key anime.
For example, variables like deathNote, attackOnTitan, swordArtOnline, angelBeats, and miraiNikki are initialized as false at the beginning of the testCSV() function. If the corresponding anime rating is found in a user's row, the respective boolean variable is set to true.

After this process was completed, I was left with a CSV file only 2 MB in length! In the future, I can continue expanding this project to  incorporate the other 16,990 shows I filtered out!

# Data Loading:
The implementation starts with loading the anime dataset from the "newAnime.csv" file using the dataLoader() function. This dataset contains information about various anime, including their genres and ratings.

# Probability Calculation: 
I first calculate probabilities using the Pandas and NumPy Python libraries. The probability tables could be separated into three groups:

1) Genre Probability Table:
The genreProbabilityTableGeneration() function generates a genre probability table based on the training data. This table maps each genre and rating combination to the probability of that rating given the genre. The structure produced was 5 unique 10 by 10 Probability Tables, stored in a Dictionary mapping a single output anime to its specific genre likelihood table.

2) Anime Probability Tables:
The animeProbabilityTableGeneration() function generates probability tables for each output anime. These tables map each input anime, score, and rating combination to the probability of that rating given the input anime. The structure produced was an embedded dictionary containing probability tables for every input output anime combination. In total, this was 25 unique 10 by 10 Probability Tables.

3) Likelihood Table:
The generateProbabilityTable() function calculates the likelihood table. This table maps each output anime to a probability vector, where each element represents the probability of a specific rating. The finished product was a single 10 by 10 probability table.

In total, I stored over 3100 probabilities in an accessible manner, each of which required many intermediate calculations computed in my helper functions. (Calcprobabilities.py, countingAnimeSpecificProbabilities.py, countingGenreProbabilities.py, probabilityFinalAnimeRating.py, and userStatistics.py).

# Recommendation Process:
The compute() function is responsible for computing the recommendation based on the user's preferences. It takes the user's input, genre probability table, anime probability tables, and likelihood table as inputs. For each output anime, it calls the compute_specific_y_givenxset() function to calculate the probability of each score.
The compute_specific_y_givenxset() function computes the probability of each score for a given output anime and user input. It multiplies the individual probabilities of the genre and input anime scores for each score rating (The program only takes rating inputs in the range 0-9, not 1-10). The final score vector is stored, and the score with the highest probability is determined.

The implementation then selects the score tuple with the highest rating and returns it as the recommendation. If multiple score tuples have the same highest rating, it selects the one with the highest percentage.



Result Presentation/Conclusion:
The resultStage() function takes the score tuple and user input as parameters. It retrieves the recommended anime name using the IDtoanime() function and presents the user with the recommendation, along with their input data. Example inputs are included in my Youtube Video! The Anime Recommender Machine Learning Model v0 utilizes the Naive Bayes algorithm to recommend anime based on user preferences and ratings. By calculating probabilities for each anime and score combination, the model determines the most suitable anime for the user. The project taught me alot how to generate probability tables, calculate likelihoods, and present recommendations based on the Naive Bayes approach. 


