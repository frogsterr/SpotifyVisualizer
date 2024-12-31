#Spotify Visualizer

## How It Works
I use OAuth2 to access Spotify's API and get User playlists aswell as song metadata.
Followingly, I grab features such as popularity and release date of songs to plot. 
Unfortunately, Spotify no longer allows you to grab song features such as dancability, energy, etc. 
What made this project particularly interesting is how I decided to create some recommendation / similarity features using the Genre tags of artists. 
I turned genre tags into word embeddigns using one-shot encoding. Then, I used PCA to reduce to the genre vector to a single-scalar value.

## How To Use
Login using OAuth and simply run the cells in the Jupyter Notebook.


## Example Output
![image](https://github.com/user-attachments/assets/0cc33782-06eb-42de-a7cf-878a02ce7453)
