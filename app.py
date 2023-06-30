
from flask import Flask, render_template, request
# import jsonify
import requests
import pickle
import numpy as np
import sklearn
from joblib import load
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = load('desiciontree.joblib')
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
   
    if request.method == 'POST':
        UNDER_CONSTRUCTION = request.form['UNDER_CONSTRUCTION']
        if(UNDER_CONSTRUCTION=='YES' or UNDER_CONSTRUCTION=='yes' or UNDER_CONSTRUCTION=='Yes'):
            UNDER_CONSTRUCTION=1
        else:
            UNDER_CONSTRUCTION=0
        RERA=request.form['RERA']
        if(RERA=='YES' or RERA=='yes' or RERA=='Yes'):
            RERA=1
        else:
            RERA=0
        BHK_NO=int(request.form['BHK_NO'])
        SQUARE_FT=float(request.form['SQUARE_FT'])
        READY_TO_MOVE=request.form['READY_TO_MOVE']
        if(READY_TO_MOVE=='YES' or READY_TO_MOVE=='yes' or READY_TO_MOVE=='Yes'):
            READY_TO_MOVE=1
        else:
            READY_TO_MOVE=0
        RESALE=request.form['RESALE']
        if(RESALE=='YES' or RESALE=='yes' or RESALE=='Yes'):
            RESALE=1
        else:
            RESALE=0
        LONGITUDE=np.log(float(request.form['LONGITUDE']))
        LATITUDE=np.log(float(request.form['LATITUDE']))
        POSTED_BY=request.form['POSTED_BY']
        if(POSTED_BY=='Builder'):
                POSTED_BY_Builder=1
                POSTED_BY_Dealer=0
                POSTED_BY_Owner=0
        elif(POSTED_BY=='Dealer') :
            POSTED_BY_Builder=0
            POSTED_BY_Dealer=1
            POSTED_BY_Owner=0
        else:
            POSTED_BY_Builder=0
            POSTED_BY_Dealer=0
            POSTED_BY_Owner=1
        BHK_OR_RK=request.form['BHK_OR_RK']
        if(BHK_OR_RK=='BHK'):
                BHK_OR_RK_BHK=1
                BHK_OR_RK_RK=0
        else:
            BHK_OR_RK_BHK=0
            BHK_OR_RK_RK=1
        CITY=request.form['CITY']
        if CITY in ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Maharashtra']:
            CITY_TIER_Tier1=1
            CITY_TIER_Tier2=0
            CITY_TIER_Tier3=0
        elif CITY in ['Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 
                  'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 
                  'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Dindigul', 'Erode', 
                  'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 
                  'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 
                  'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 
                  'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Mangalore', 'Meerut', 'Moradabad', 
                  'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Pondicherry', 'Purulia', 'Prayagraj', 
                  'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Ratlam', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 
                  'Solapur', 'Srinagar', 'Surat', 'Thanjavur', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 
                  'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 
                  'Vellore', 'Warangal']:
            CITY_TIER_Tier1=0
            CITY_TIER_Tier2=1
            CITY_TIER_Tier3=0
        else:
            CITY_TIER_Tier1=0
            CITY_TIER_Tier2=0
            CITY_TIER_Tier3=1
        
        
        
        
        
        
        
        
        
        prediction=model.predict([[UNDER_CONSTRUCTION,RERA,BHK_NO,SQUARE_FT,READY_TO_MOVE,RESALE,LONGITUDE,LATITUDE, POSTED_BY_Builder, POSTED_BY_Dealer, POSTED_BY_Owner,BHK_OR_RK_BHK,BHK_OR_RK_RK, CITY_TIER_Tier1, CITY_TIER_Tier2, CITY_TIER_Tier3]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this House")
        else:
            return render_template('index.html',prediction_text="You Can Sell Your House at {} lakh.".format(output))
       
    else:
        return render_template('index.html')
     
     

if __name__=="__main__":
    app.run(debug=True)