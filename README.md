## How It Works
I use OAuth2 to access Spotify's API and get User playlists and song metadata.
Followingly, I grab features such as popularity and release date of songs to plot. 
Unfortunately, Spotify no longer lets you grab song features such as danceability, energy, etc. 
What made this project particularly interesting was my decision to create some recommendation/similarity features using artists' Genre tags. 
I turned genre tags into word embeddings using one-shot encoding. Then, I used PCA to reduce the genre vector to a single-scalar value.

## How To Use
Login using OAuth and simply run the cells in the Jupyter Notebook.


## Example Output
![image](https://github.com/user-attachments/assets/0cc33782-06eb-42de-a7cf-878a02ce7453)
