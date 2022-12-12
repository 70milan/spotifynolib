--The spotify file tries to fetch the "saved songs" api from my spotify account to get a list of all the tracks 
  that I have added over the duration of 6 years.
--The objective of this project is to get parameters from the user's playlist of "liked songs" such as:

	song_name, artist_name, genre, date_added, mood, dancebility

-- The code was written without utilizing any third-party spotify modules

(there are almost 700 liked songs that have been added to the playlist over the years.)

-- These params will be used to analyze the patterns such as:
	-- favourite genre of the user
	-- fav artists
	-- what was the "genre" of the majority of the songs that were added to the playlist in a given year?
	-- what was the "dancilibity" score and "mood" of the songs that were added to the playlist over the years years?
	-- how the pattern of "dancilibity" score and "mood" of the songs changed over the years 
	   and what information it provides about the user's personality.
		 
	 

Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

Acousticness: A measure from 0.0 to 1.0 of whether the track is acoustic.

Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.

Instrumentalness: Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.

Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live.

Loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track. Values typical range between -60 and 0 db.

Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value.

Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.

Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).