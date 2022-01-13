from App.applib.Core.analyser import Detector



DetectedFrequency = 0

def DetectFrequency():
    detector = Detector()
    detectFrequency = detector.start_detection()
    while True:
        DetectedFrequency = detectFrequency.__next__()
