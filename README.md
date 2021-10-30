# optimizedSTT
This is a Speech to Text  program. 
It was made with the library called SpeechRecognition.<br>
<br>
I the biggest problem I faced while using the library is, the the value of Energy Threshold would keep going lower while performing recognizer_instance.listen() function. Even lower than the ambient noise of the surrounding. while this value goes lower than the ambient noise the function keeps recording sound until it reaches pause_threshold, which is not likely to happen most of the time is energy_threshold is lower than the ambient noise. <br>
So, I had to develop an idea, so the energy threshold would be higher than the ambient noise. This is not as easy as it sounds. As the dynamic_energy_ratio had to be different for different level of ambient noise, Like for ambient noise of 40-80 dynamic_energy_ratio could be as high as 5-8 times where for ambient noise of 1500 or higher the ratio could be about 1.5 and I can't just put all these values manually which would give me a really inconsistent result. So, I tried to develop a simple formula.<br>
