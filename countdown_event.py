def countdown_event(series, num_days):
# Function to countdown the nummber of days before and after an event
# Days before are negative, days after are positive, event days are 0 and other days are null
# Params:
# series - Series with event flag (1 for event days and 0 for other days)
# num_days - Number of days before and after to count down
# Returns numpy array

    array = series.replace({0: 99, 1: 0}) # Replace with 99 instead of np.nan as np.nan doesn't seem to work in the if statement below
    for index, value in enumerate(array):
        # Countdown days before
        try:
            if value == 0 and array[index - 1] == 99:
                for i in range(num_days):
                    array[index - (i + 1)] = -(i + 1)
                    array[index + (i + 1)] = (i + 1)
        except:
            pass
        # Replace 99 with null
        array_nan = [i if i != 99 else np.nan for i in array]
    return array_nan