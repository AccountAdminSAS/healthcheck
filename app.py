from flask import Flask, render_template, jsonify, request, session, url_for
from data import library_data, questions, tracking_questions

app = Flask(__name__)
app.secret_key = "010101"


# Main route (index)
@app.route("/index")
def index():
    score = session.get("score", None)
    return render_template("index.html", score=score)

# Correct route for Resources.html
@app.route("/resources")
def resources():
    return render_template("Resources.html")

#route for trackpage
@app.route("/TrackPage.html", methods=["GET", "POST"])
def trackpage():
    score = session.get("score", None)
    old_score = 0  # Initialise old score
    bmi_result = None  # Initialise the result of the BMI calculation
    submitted = False
    x_position = 175
    bmi = None


    # Initialise flagged_responses as an empty dictionary 
    flagged_responses = session.get("flagged_responses", {})
    tracking_flagged_responses = session.get("tracking_flagged_responses", {})

    if request.method == "POST":
        submitted = True
        # Clear previous flagged responses from the session
        tracking_flagged_responses.clear()

        for question in tracking_questions:
            selected_value = request.form.get(question["id"], "0")  # Default to "0" if not selected

            if question["type"] == "fitness":
                # Convert to integer and add to score
                old_score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "20":
                    tracking_flagged_responses[question["id"]] = "If you don’t engage in physical activity each week, consider starting with short daily walks or light stretching. Regular movement improves heart health, mood, and energy levels. Even small changes can make a big difference!"

                elif selected_value == "-20":
                    tracking_flagged_responses[question["id"]] = "Regular physical activity is essential for cardiovascular health, weight management, and mental well-being. A completely sedentary lifestyle increases the risk of conditions like heart disease, diabetes, and muscle loss. If you find it hard to exercise, start with small, manageable steps—such as a 5–10 minute walk daily or stretching in the morning. Gradually increasing your activity level can improve your energy, mood, and overall health. If mobility is a concern, low-impact exercises like swimming or chair yoga may be beneficial."
    
            elif question["type"] == "strength":
                # Convert to integer and add to score
                old_score += int(selected_value)

                if selected_value == "10":
                    tracking_flagged_responses[question["id"]] = "Strength training is essential for maintaining muscle mass and bone health. If you’re not currently doing any, consider incorporating bodyweight exercises like squats, lunges, or push-ups twice a week. It’s never too late to start!"

                elif selected_value == "-10":
                    tracking_flagged_responses[question["id"]] = "Strength training is crucial for maintaining muscle mass, bone density, and metabolic health, especially as you age. A lack of resistance exercises can lead to muscle atrophy, increased injury risk, and poor posture. Strength training doesn’t have to mean lifting heavy weights—bodyweight exercises like squats, push-ups, or resistance bands can be highly effective. Even just two 20-minute sessions per week can make a big difference. Consider integrating simple movements into your routine, like standing up from a chair without using your hands or carrying groceries instead of using a cart."

            elif question["type"] == "sitting":
                old_score += int(selected_value)

                if selected_value == "50":
                    tracking_flagged_responses[question["id"]] = "Sitting for long hours can negatively impact posture, circulation, and overall health. Try to take short breaks to stand up and stretch every hour, and if possible, include some light movement during the day."

                elif selected_value == "5":
                    tracking_flagged_responses[question["id"]] = "Prolonged sitting has been linked to increased risks of obesity, heart disease, and poor circulation. If you’re sitting for the majority of your day without movement breaks, it can lead to back pain, reduced metabolism, and poor posture. Try setting a reminder to stand up and stretch every 30–60 minutes, even if just for a minute or two. If possible, consider a standing desk or walking meetings. Simple habits like taking the stairs instead of the elevator or parking farther away can add more movement to your day."

            elif question["type"] == "sleep":
                old_score += int(selected_value)

                if selected_value == "30":
                    tracking_flagged_responses[question["id"]] = "Getting enough sleep is crucial for your overall well-being. If you’re not averaging at least 7 hours per night, consider improving your sleep routine by reducing screen time before bed, maintaining a consistent schedule, and creating a relaxing environment."

                elif selected_value == "-10":
                    tracking_flagged_responses[question["id"]] = "Consistently sleeping fewer than 5 hours can have severe consequences for cognitive function, immune health, and emotional stability. Chronic sleep deprivation increases the risk of heart disease, obesity, and mental health struggles. If you struggle with sleep, try establishing a wind-down routine—dim the lights, avoid screens an hour before bed, and maintain a consistent sleep schedule. If stress or anxiety is preventing rest, relaxation techniques like deep breathing or meditation may help. If sleep issues persist, consider consulting a healthcare professional to rule out underlying conditions such as sleep apnea or insomnia. "

            elif question["type"] == "water":
                old_score += int(selected_value)

                if selected_value == "5":
                    tracking_flagged_responses[question["id"]] = "Dehydration can lead to fatigue, headaches, poor digestion, and even kidney problems. Water is essential for nearly every function in your body, including temperature regulation and nutrient transport. If you struggle to drink enough, try keeping a water bottle with you at all times, setting reminders, or adding natural flavors (like lemon or cucumber) to make it more appealing. If you consume a lot of caffeine or alcohol, your hydration needs increase, so balancing intake is key."

            elif question["type"] == "mental":
                old_score += int(selected_value)

                if selected_value == "80":
                    tracking_flagged_responses[question["id"]] = "Feeling persistently sad or anxious can be overwhelming. If this has been a recurring issue, consider talking to a trusted friend, practicing mindfulness, or seeking professional support. You don’t have to go through it alone."

                elif selected_value == "5":
                    tracking_flagged_responses[question["id"]] = "Experiencing frequent sadness or anxiety can be overwhelming and may indicate underlying stressors or mental health conditions such as depression or anxiety disorders. It’s important to acknowledge these feelings and seek support. Consider speaking to a mental health professional, journaling your thoughts, practicing mindfulness, or engaging in activities that bring you joy. Social support is crucial, so don’t hesitate to reach out to trusted friends or family members. If your emotions are interfering with daily life, professional help can offer valuable tools to navigate these challenges."

            elif question["type"] == "smoke":
                old_score += int(selected_value)

                if selected_value == "-10":
                    tracking_flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

                elif selected_value == "-30":
                    tracking_flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

                elif selected_value == "-50":
                    tracking_flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

                elif selected_value == "-100":
                    tracking_flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

            elif question["type"] == "alcohol":
                old_score += int(selected_value)

                if selected_value == "5":
                    tracking_flagged_responses[question["id"]] = "Excessive alcohol intake can affect sleep, liver health, and overall well-being. If you consume alcohol regularly, consider moderating your intake and balancing it with a healthy lifestyle."

                elif selected_value == "-35":
                    tracking_flagged_responses[question["id"]] = "Excessive alcohol consumption can negatively impact liver health, mental clarity, sleep quality, and overall well-being. Regular heavy drinking increases the risk of high blood pressure, digestive issues, and addiction. If alcohol is a significant part of your routine, consider setting limits or incorporating alcohol-free days into your week. Seeking healthier ways to unwind like exercise, hobbies, or meditation can reduce dependence on alcohol for stress relief. If cutting back feels challenging, professional guidance or support groups can be beneficial in finding a balance that supports your long-term health. "

                elif selected_value == "-100":
                    tracking_flagged_responses[question["id"]] = "Excessive alcohol consumption can negatively impact liver health, mental clarity, sleep quality, and overall well-being. Regular heavy drinking increases the risk of high blood pressure, digestive issues, and addiction. If alcohol is a significant part of your routine, consider setting limits or incorporating alcohol-free days into your week. Seeking healthier ways to unwind like exercise, hobbies, or meditation can reduce dependence on alcohol for stress relief. If cutting back feels challenging, professional guidance or support groups can be beneficial in finding a balance that supports your long-term health. "

            else:
                # Handle other question types
                old_score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "10":
                    tracking_flagged_responses[question["id"]] = "This response is 10. Thank you for rating!"


        # Store score, BMI result, and flagged responses in session
        session["score"] = score  
        session["old_score"] = old_score  
        session["bmi_result"] = bmi_result
        session["flagged_responses"] = flagged_responses  
        session["tracking_flagged_responses"] = tracking_flagged_responses

    # Ensure bmi_result is always available from the session
    bmi_result = session.get("bmi_result", None)

    return render_template(
        "TrackPage.html", 
        tracking_questions=tracking_questions, 
        old_score=session.get("old_score"),
        score = score,
        bmi_result=bmi_result,
        submitted=submitted,
        flagged_responses=flagged_responses,
        tracking_flagged_responses=tracking_flagged_responses,
        bmi=bmi, x_position=x_position
    )

#route for assessment
@app.route("/AssessmentPage.html", methods=["GET", "POST"])
def assessmentpage():
    session.clear()  # Clear session data for fresh assessment
    score = 0  # Initialize score
    bmi_result = None  # Initialize the result of the BMI calculation
    submitted = False
    x_position = 50
    bmi = None

    # Initialise flagged_responses as an empty dictionary 
    flagged_responses = session.get("flagged_responses", {})

    if request.method == "POST":
        submitted = True
        # Clear previous flagged responses from the session
        flagged_responses.clear()


        for question in questions:
            selected_value = request.form.get(question["id"], "0")  # Default to "0" if not selected

            if question["type"] == "fitness":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "20":
                    flagged_responses[question["id"]] = "If you don’t engage in physical activity each week, consider starting with short daily walks or light stretching. Regular movement improves heart health, mood, and energy levels. Even small changes can make a big difference!"

                elif selected_value == "-20":
                    flagged_responses[question["id"]] = "Regular physical activity is essential for cardiovascular health, weight management, and mental well-being. A completely sedentary lifestyle increases the risk of conditions like heart disease, diabetes, and muscle loss. If you find it hard to exercise, start with small, manageable steps—such as a 5–10 minute walk daily or stretching in the morning. Gradually increasing your activity level can improve your energy, mood, and overall health. If mobility is a concern, low-impact exercises like swimming or chair yoga may be beneficial."
    
            elif question["type"] == "strength":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "10":
                    flagged_responses[question["id"]] = "Strength training is essential for maintaining muscle mass and bone health. If you’re not currently doing any, consider incorporating bodyweight exercises like squats, lunges, or push-ups twice a week. It’s never too late to start!"

                elif selected_value == "-10":
                    flagged_responses[question["id"]] = "Strength training is crucial for maintaining muscle mass, bone density, and metabolic health, especially as you age. A lack of resistance exercises can lead to muscle atrophy, increased injury risk, and poor posture. Strength training doesn’t have to mean lifting heavy weights—bodyweight exercises like squats, push-ups, or resistance bands can be highly effective. Even just two 20-minute sessions per week can make a big difference. Consider integrating simple movements into your routine, like standing up from a chair without using your hands or carrying groceries instead of using a cart."

            elif question["type"] == "sitting":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "50":
                    flagged_responses[question["id"]] = "Sitting for long hours can negatively impact posture, circulation, and overall health. Try to take short breaks to stand up and stretch every hour, and if possible, include some light movement during the day."

                elif selected_value == "5":
                    flagged_responses[question["id"]] = "Prolonged sitting has been linked to increased risks of obesity, heart disease, and poor circulation. If you’re sitting for the majority of your day without movement breaks, it can lead to back pain, reduced metabolism, and poor posture. Try setting a reminder to stand up and stretch every 30–60 minutes, even if just for a minute or two. If possible, consider a standing desk or walking meetings. Simple habits like taking the stairs instead of the elevator or parking farther away can add more movement to your day."

            elif question["type"] == "sleep":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "30":
                    flagged_responses[question["id"]] = "Getting enough sleep is crucial for your overall well-being. If you’re not averaging at least 7 hours per night, consider improving your sleep routine by reducing screen time before bed, maintaining a consistent schedule, and creating a relaxing environment."

                elif selected_value == "-10":
                    flagged_responses[question["id"]] = "Consistently sleeping fewer than 5 hours can have severe consequences for cognitive function, immune health, and emotional stability. Chronic sleep deprivation increases the risk of heart disease, obesity, and mental health struggles. If you struggle with sleep, try establishing a wind-down routine—dim the lights, avoid screens an hour before bed, and maintain a consistent sleep schedule. If stress or anxiety is preventing rest, relaxation techniques like deep breathing or meditation may help. If sleep issues persist, consider consulting a healthcare professional to rule out underlying conditions such as sleep apnea or insomnia. "

            elif question["type"] == "water":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "5":
                    flagged_responses[question["id"]] = "Dehydration can lead to fatigue, headaches, poor digestion, and even kidney problems. Water is essential for nearly every function in your body, including temperature regulation and nutrient transport. If you struggle to drink enough, try keeping a water bottle with you at all times, setting reminders, or adding natural flavors (like lemon or cucumber) to make it more appealing. If you consume a lot of caffeine or alcohol, your hydration needs increase, so balancing intake is key."

            elif question["type"] == "mental":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "80":
                    flagged_responses[question["id"]] = "Feeling persistently sad or anxious can be overwhelming. If this has been a recurring issue, consider talking to a trusted friend, practicing mindfulness, or seeking professional support. You don’t have to go through it alone."

                elif selected_value == "5":
                    flagged_responses[question["id"]] = "Experiencing frequent sadness or anxiety can be overwhelming and may indicate underlying stressors or mental health conditions such as depression or anxiety disorders. It’s important to acknowledge these feelings and seek support. Consider speaking to a mental health professional, journaling your thoughts, practicing mindfulness, or engaging in activities that bring you joy. Social support is crucial, so don’t hesitate to reach out to trusted friends or family members. If your emotions are interfering with daily life, professional help can offer valuable tools to navigate these challenges."

            elif question["type"] == "smoke":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "-10":
                    flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

                elif selected_value == "-30":
                    flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

                elif selected_value == "-50":
                    flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

                elif selected_value == "-100":
                    flagged_responses[question["id"]] = "Frequent smoking or vaping significantly increases the risk of lung disease, heart conditions, and long-term addiction. Nicotine affects brain function, increases stress levels over time, and can lead to dependence. If quitting feels overwhelming, start with small reductions and set achievable goals. Many support programs, nicotine replacement therapies, and behavioral strategies can help. Replacing the habit with healthier alternatives like chewing gum, deep breathing exercises, or engaging in a physical activity can make the transition easier. Your body begins to heal as soon as you cut back, so any reduction is a step in the right direction."

            elif question["type"] == "alcohol":
                # Convert to integer and add to score
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "5":
                    flagged_responses[question["id"]] = "Excessive alcohol intake can affect sleep, liver health, and overall well-being. If you consume alcohol regularly, consider moderating your intake and balancing it with a healthy lifestyle."

                elif selected_value == "-35":
                    flagged_responses[question["id"]] = "Excessive alcohol consumption can negatively impact liver health, mental clarity, sleep quality, and overall well-being. Regular heavy drinking increases the risk of high blood pressure, digestive issues, and addiction. If alcohol is a significant part of your routine, consider setting limits or incorporating alcohol-free days into your week. Seeking healthier ways to unwind like exercise, hobbies, or meditation can reduce dependence on alcohol for stress relief. If cutting back feels challenging, professional guidance or support groups can be beneficial in finding a balance that supports your long-term health. "

                elif selected_value == "-100":
                    flagged_responses[question["id"]] = "Excessive alcohol consumption can negatively impact liver health, mental clarity, sleep quality, and overall well-being. Regular heavy drinking increases the risk of high blood pressure, digestive issues, and addiction. If alcohol is a significant part of your routine, consider setting limits or incorporating alcohol-free days into your week. Seeking healthier ways to unwind like exercise, hobbies, or meditation can reduce dependence on alcohol for stress relief. If cutting back feels challenging, professional guidance or support groups can be beneficial in finding a balance that supports your long-term health. "

            else:
                # Handle other question types
                score += int(selected_value)

                # Flag responses where value is "10"
                if selected_value == "10":
                    flagged_responses[question["id"]] = "A rating of 10 means you are amazing!."

                # Perform BMI calculation with weight and height are provided
                weight = request.form.get("weight")
                height = request.form.get("height")

        if weight and height:
            try:
                weight = float(weight)  # Weight in kilograms
                height = float(height) / 100  # Convert to meters
                if weight <= 0 or height <= 0:
                    bmi_result = "Invalid input: Weight and height must be positive numbers."
                else:
                    bmi_value = weight / (height ** 2)
                    bmi_result = round(bmi_value, 1)
                    # Get weight and height from form
                    weight = float(request.form['weight'])
                    height = float(request.form['height']) / 100  # Convert cm to meters
                    bmi = weight / (height ** 2)
        
                    # Calculate X position based on BMI
                    min_bmi, max_bmi = 10, 40  # Minimum and Maximum expected BMI
                    min_x, max_x = 50, 450  # X-axis position range for the chart
        
                    # Map the BMI to X-axis position
                    x_position = min_x + (bmi - min_bmi) / (max_bmi - min_bmi) * (max_x - min_x)
                    x_position = max(min_x, min(x_position, max_x))  # Ensure it's within bounds
            except ValueError:
                bmi_result = "Invalid input for BMI calculation"

            



        # Store score, BMI result, and flagged responses in session
        session["score"] = score  
        session["bmi_result"] = bmi_result
        session["flagged_responses"] = flagged_responses  

    # Ensure bmi_result is always available from the session
    bmi_result = session.get("bmi_result", None)

    return render_template(
        "AssessmentPage.html", 
        questions=questions, 
        score=session.get("score"),
        bmi_result=bmi_result,
        submitted=submitted,
        flagged_responses=flagged_responses,
        bmi=bmi, x_position=x_position
    )



# Function to flag a response and store it in the dictionary
def flag_response(answer, info):
    flagged_responses[answer] = info


def tracking_flag_response(answer, info):
    tracking_flagged_responses[answer] = info


#Route for data
@app.route("/data")
def get_data():
    return jsonify(library_data)  # Returning the data as JSON

if __name__ == "__main__":
    app.run(debug=True)