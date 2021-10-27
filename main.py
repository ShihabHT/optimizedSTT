# Trying to separate voice from ambient noise
import speech_recognition as sr

r = sr.Recognizer()
# r.energy_threshold = 2700
r.dynamic_energy_threshold = True
r.dynamic_energy_adjustment_damping = 0.15
r.dynamic_energy_ratio = 1
print(r.pause_threshold)
print("Dynamic Energy threshold :", r.dynamic_energy_threshold)
print("Dynamic Energy adjustment Damping :", r.dynamic_energy_adjustment_damping)

while True:
    print("\nEnergy threshold before adjusting :", r.energy_threshold)
    with sr.Microphone() as source:
        r.dynamic_energy_ratio = 1
        print("Dynamic Energy ratio before adjusting :", r.dynamic_energy_ratio)
        r.adjust_for_ambient_noise(source, 1)
        graph_ratio = 41.264 * (r.energy_threshold ** -0.443)
        r.dynamic_energy_ratio = graph_ratio
        print("Energy threshold before multiplying :", r.energy_threshold)
        # r.energy_threshold = r.energy_threshold * graph_ratio
        print("Energy threshold after adjusting :", r.energy_threshold)
        print("Dynamic Energy ratio :", r.dynamic_energy_ratio)
        speech = r.listen(source, phrase_time_limit=10)
        print("Energy threshold after listening :", r.energy_threshold)
        print("Dynamic Energy ratio after listening :", r.dynamic_energy_ratio)

        try:
            txt = r.recognize_google(speech)
        except sr.UnknownValueError:
            txt = "Null"
        except sr.RequestError:
            txt = "Sorry, my speech service is down!"
        except sr.WaitTimeoutError:
            txt = "Timed out!"

    print(txt)