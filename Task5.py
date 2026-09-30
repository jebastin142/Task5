total_days = 20
rain_days = 8
not_rain_days = 12

cloudy_given_rain_days = 7
cloudy_given_not_rain_days = 3

p_rain = rain_days / total_days
p_not_rain = not_rain_days / total_days

p_cloudy_given_rain = cloudy_given_rain_days / rain_days
p_cloudy_given_not_rain = cloudy_given_not_rain_days / not_rain_days

p_cloudy = (p_cloudy_given_rain * p_rain) + (p_cloudy_given_not_rain * p_not_rain)

p_rain_given_cloudy = (p_cloudy_given_rain * p_rain) / p_cloudy
p_not_rain_given_cloudy = (p_cloudy_given_not_rain * p_not_rain) / p_cloudy

if p_rain_given_cloudy > p_not_rain_given_cloudy:
    prediction = "Rain"
else:
    prediction = "Not Rain"

print("Dataset")
print("-" * 40)
print("Total Days           =", total_days)
print("Rain Days            =", rain_days)
print("Not Rain Days        =", not_rain_days)
print("Cloudy on Rain Days  =", cloudy_given_rain_days)
print("Cloudy on Dry Days   =", cloudy_given_not_rain_days)

print("\nProbabilities")
print("-" * 40)
print("P(Rain)              = {:.4f}".format(p_rain))
print("P(Not Rain)          = {:.4f}".format(p_not_rain))
print("P(Cloudy | Rain)     = {:.4f}".format(p_cloudy_given_rain))
print("P(Cloudy | Not Rain) = {:.4f}".format(p_cloudy_given_not_rain))
print("P(Cloudy)            = {:.4f}".format(p_cloudy))
print("P(Rain | Cloudy)     = {:.4f}".format(p_rain_given_cloudy))
print("P(Not Rain | Cloudy) = {:.4f}".format(p_not_rain_given_cloudy))

print("\nPrediction (Sky = Cloudy)")
print("-" * 40)
print("Predicted Weather    =", prediction)