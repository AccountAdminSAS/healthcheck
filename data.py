
library_data = {
    "Smoking Addiction": "Quitting smoking improves health, reduces disease risk, and enhances quality of life. Immediate benefits include lower heart rate and normalised carbon monoxide levels, while long-term benefits include a reduced risk of heart disease and lung cancer. Effective quitting methods include cold turkey, nicotine replacement therapy (NRT), medications like varenicline or bupropion, behavioral support, and gradual reduction. Common withdrawal symptoms include irritability, cravings, sleep issues, and increased appetite. To succeed, find motivation, avoid triggers, seek support, stay busy, and reward progress. Start your quit journey today for a healthier future.   Read more about how to quit smoking. Learn more at <a href='https://www.nhs.uk/better-health/quit-smoking/?WT.mc_ID=PPC_CORE_SMOKING_2425&wt.tsrc=paid_search&gad_source=1&gclid=CjwKCAiAnKi8BhB0EiwA58DA4WaxmVQVPOalSWdMx_21JibvRZwtNkAMiiD0WSf7_b2QpoEQpWjcqxoCr6IQAvD_BwE&gclsrc=aw.ds' target='_blank'>Read more</a>.",
    "Physical Activity": "Increasing physical activity boosts overall health, reduces disease risk, and enhances mental well-being. Immediate benefits include improved mood and increased energy, while long-term benefits include better heart health, stronger muscles, and reduced risk of chronic diseases. Effective ways to increase activity include setting realistic goals, incorporating movement into daily routines, engaging in enjoyable activities, and gradually increasing intensity. Common challenges include lack of time, motivation, and energy, which can be overcome by planning workouts, finding support, and making exercise a habit. To succeed, stay consistent, track progress, and celebrate achievements. Resources like fitness apps, online workouts, and community programs offer additional support. Start moving today for a healthier future. Explore your daily requirements to stay on top of your health. <a href='https://www.who.int/news-room/fact-sheets/detail/physical-activity#:~:text=Physical%20activity%20refers%20to%20all,intensity%20physical%20activity%20improve%20health.' target='_blank'>Read more</a>.",
    "BMI Benefits & Limitations": "Body Mass Index (BMI) is a simple tool to assess weight status and potential health risks. Benefits include its ease of use, cost-effectiveness, and ability to provide a general indication of health risks related to underweight, overweight, and obesity. However, limitations exist as BMI does not differentiate between muscle and fat, nor does it consider factors like age, gender, ethnicity, and body composition. It may misclassify athletes and certain populations. To get a more accurate health assessment, complement BMI with other measures like lifestyle evaluations. Understanding both its benefits and limitations ensures better health insights. Read about BMI limitations <a href='https://www.bbc.co.uk/bitesize/guides/zfc3pg8/revision/6#:~:text=BMI%20cannot%20tell%20the%20difference,age%2C%20gender%20or%20muscle%20mass.' target='_blank'>Read more</a>.",
    "Strength Training": "Strength training enhances muscle strength, endurance, and overall health. Benefits include improved metabolism, bone density, joint support, and reduced risk of chronic diseases like osteoporosis and diabetes. It helps with weight management, boosts mental well-being, and enhances daily functional movements. Effective strength training involves resistance exercises using body weight, free weights, machines, or resistance bands. Key principles include proper form, progressive overload, and consistency. Common challenges like lack of time or knowledge can be overcome with structured programs, professional guidance, and gradual progression. Resources like fitness apps, online tutorials, and personal trainers offer additional support. Start strength training today for a healthier, stronger future.",
    "Prolonged Sitting": "Prolonged sitting negatively impacts overall health, increasing the risk of obesity, heart disease, diabetes, and musculoskeletal issues. It can lead to poor posture, reduced circulation, and lower energy levels. Breaking up long sitting periods with short movement breaks, stretching, or standing desks can help mitigate these risks. Regular physical activity, such as walking, strength training, or flexibility exercises, counteracts the negative effects. Developing habits like setting movement reminders, using active workstations, and incorporating more standing activities into daily routines can improve well-being. Reducing prolonged sitting contributes to better posture, circulation, and overall health.",
    "Sleep": "Quality sleep is essential for overall health, supporting cognitive function, immune health, and emotional well-being. Poor sleep is linked to increased risks of obesity, heart disease, diabetes, and mental health disorders. Establishing a consistent sleep schedule, creating a relaxing bedtime routine, and optimising the sleep environment with comfortable bedding and minimal distractions can improve sleep quality. Reducing screen time before bed, managing stress, and limiting caffeine intake in the evening further enhance restfulness. Prioritising sufficient, high-quality sleep leads to better focus, mood regulation, and overall well-being.",
    "Hydration": "Drinking enough water is vital for overall health, supporting digestion, circulation, temperature regulation, and cognitive function. Dehydration can lead to fatigue, headaches, poor concentration, and increased risk of kidney stones and other health issues. Proper hydration boosts energy levels, improves skin health, and aids in nutrient absorption. To stay hydrated, drink water regularly throughout the day, especially before meals and after physical activity. Reducing sugary drinks and consuming water-rich foods like fruits and vegetables can further enhance hydration. Prioritising adequate water intake contributes to better overall health and well-being."
}

flagged_questions = [{"id": "005", "text": "How often do you currently engage in physical activity or exersice per week?", "type": "fitness"},
                     {"id": "006", "text": "Do you currently perform any strength-training exersices? If yes, how many times per week? ", "type": "strength"},
                     {"id": "007", "text": "On avarage, how much time are you currently sitting in a chair per day?", "type": "sitting"},
                     {"id": "008", "text": "How many hours of sleep do you currently get of avarage each night?", "type": "sleep"},
                     {"id": "009", "text": "Do you currently drink at least 2 Liters of water each day?", "type": "water"},
                     {"id": "012", "text": "How often have you felt persistently sad or anxious in the past month?", "type": "mental"},
                     {"id": "013", "text": "Do you currently smoke or use tobacco or vape products? If yes, how often per week?", "type": "smoke"},
                     {"id": "014", "text": "Do you currently consume alcoholic drinks? If yes, how many units per week?", "type": "alcohol"},
    ]
    
questions = [
    {"id": "001", "text": "What is your age?", "type": "age"},  
    {"id": "002", "text": "What is your height?", "type": "integer"},  # Number input
    {"id": "003", "text": "What is your weight?", "type": "integer"},  # Number input
    {"id": "004", "text": "Do you have any known chronic health conditions?", "type": "healthcondition"},  
    {"id": "005", "text": "How often do you currently engage in physical activity or exersice per week?", "type": "fitness"},
    {"id": "006", "text": "Do you currently perform any strength-training exersices? If yes, how many times per week? ", "type": "strength"},
    {"id": "007", "text": "On avarage, how much time are you currently sitting in a chair per day?", "type": "sitting"},
    {"id": "008", "text": "How many hours of sleep do you currently get of avarage each night?", "type": "sleep"},
    {"id": "009", "text": "Do you currently drink at least 2 Liters of water each day?", "type": "water"},
    {"id": "010", "text": "How many processed or fast-food meals do you consume per week?", "type": "badfood"},
    {"id": "011", "text": "How many servings of fruit and vegetables do you consume daily?", "type": "goodfood"},
    {"id": "012", "text": "How often have you felt persistently sad or anxious in the past month?", "type": "mental"},
    {"id": "013", "text": "Do you currently smoke or use tobacco or vape products? If yes, how often per week?", "type": "smoke"},
    {"id": "014", "text": "Do you currently consume alcoholic drinks? If yes, how many units per week?", "type": "alcohol"},
    {"id": "015", "text": "Do you use recreational drugs or substances? If yes, how many times per week?", "type": "drugs"},
    {"id": "016", "text": "How would you rate your overall health on a scale of 1-10", "type": "rating"},
    {"id": "017", "text": "What area of health would you like to improve the most?", "type": "choice"},
]

tracking_questions = [
    {"id": "505", "text": "What was your physical activity or exercise level per week?", "type": "fitness"},
    {"id": "506", "text": "What was your level of strength training exercise?", "type": "strength"},
    {"id": "507", "text": "What was your avarage time sitting in a chair per day?", "type": "sitting"},
    {"id": "508", "text": "How many hours of sleep did you get?", "type": "sleep"},
    {"id": "509", "text": "Did you drink at least 2 Liters of water?", "type": "water"},
    {"id": "510", "text": "How often did you feel persistently sad or anxious?", "type": "mental"},
    {"id": "511", "text": "How often did you smoke or use anytobacco or vape products per week?", "type": "smoke"},
    {"id": "512", "text": "How many units of alcohol did you consume per week?", "type": "alcohol"}







    ]
