Purpose(s) of each service
--------------------------------
Audio Conversion Service
    * normalizes the raw uploaded audio file to a uniform format for later comparison
    * ShazamService uses this synchronous call and stores the result
   
Shazam Service
    * answers LIST requests and various GET requests (artist, lyrics, 3rd party redirects)
    * requests the AudioConversionService to convert the mp3 to a uniform format

Audio Comparison Service
    * compares the converted audio against the repository of songs and returns a match if it exists otherwise times out
