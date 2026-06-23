"""ACSST Session 4"""

def estimate_vo2(distance_km):
    return round((distance_km * 1000 - 504.9) / 44.73, 1)
print(estimate_vo2(1))

def calculate_trimp(avg_hr, max_hr, duration):

    ratio = avg_hr / max_hr

    trimp = duration * ratio * 0.64 * 2.718 ** (1.92 * ratio)

    return round(trimp, 2)
print(calculate_trimp(150, 190, 60))

def analyze_sprint(splits):
    distances = [10, 20, 30] # meters
    return [round(d / t, 1) for d, t in zip(distances, splits)]
print (analyze_sprint([100, 200, 300]))
print (analyze_sprint([200, 400, 600]))

def assess_risk(weight, height):

    bmi = weight / (height ** 2)

    if bmi < 18.5:

        return "Underweight - High injury risk"

    elif 18.5 <= bmi < 25:

        return "Normal - Low risk"

    else:

        return "Overweight - Moderate risk"
print(assess_risk(70, 1.68))
print(assess_risk(79, 1.78))

def analyze_sprint(splits):
    """
    Given a list of split times (in seconds) for distances [10m, 20m, 30m],
    return a list of average speeds (m/s), rounded to 1 decimal place.
    """
    distances = [10, 20, 30]  # meters
    speeds = []

    for dist, time in zip(distances, splits):
        speed = dist / time
        speeds.append(round(speed, 1))

    return speeds
print(analyze_sprint([1.5,1.2,1,1]))