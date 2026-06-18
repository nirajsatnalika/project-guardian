
# kyc.py

import random
import pandas as pd


class KYC:


    def __init__(self):

        self.records={}



    #####################################
    # PAN Validation
    #####################################


    def validate_pan(

            self,

            pan

    ):


        pan=pan.upper()


        if len(pan)!=10:

            return False


        if not pan[:5].isalpha():

            return False


        if not pan[5:9].isdigit():

            return False


        if not pan[-1].isalpha():

            return False


        return True



    #####################################
    # Aadhaar Validation
    #####################################


    def validate_aadhaar(

            self,

            aadhaar

    ):



        aadhaar=str(aadhaar)


        if len(aadhaar)==12 and aadhaar.isdigit():

            return True


        return False




    #####################################
    # Dummy Face Match
    #####################################


    def face_match(

            self,

            selfie_file=None

    ):



        score=random.randint(

        85,

        99

        )



        return {

        "verified":

        True,



        "score":

        score

        }




    #####################################
    # Email OTP
    #####################################



    def email_otp(

            self,

            email

    ):



        otp=random.randint(

        100000,

        999999

        )



        return otp




    #####################################
    # Complete KYC
    #####################################



    def verify_kyc(

            self,

            name,

            pan,

            aadhaar,

            email

    ):



        pan_ok=self.validate_pan(

        pan

        )



        aadhaar_ok=self.validate_aadhaar(

        aadhaar

        )



        face=self.face_match()



        face_ok=face["verified"]



        if pan_ok and aadhaar_ok and face_ok:



            status="VERIFIED"



        else:



            status="FAILED"




        self.records[name]={



        "name":

        name,



        "pan":

        pan,



        "aadhaar":

        aadhaar,



        "email":

        email,



        "pan_verified":

        pan_ok,



        "aadhaar_verified":

        aadhaar_ok,



        "face_verified":

        face_ok,



        "face_score":

        face["score"],



        "status":

        status

        }



        return self.records[name]




    #####################################
    # Check Existing KYC
    #####################################



    def get_kyc(

            self,

            name

    ):



        return self.records.get(

        name,

        None

        )





    #####################################
    # Get All KYC
    #####################################



    def get_dataframe(self):



        if len(

        self.records

        )==0:



            return pd.DataFrame()



        return pd.DataFrame(

        self.records

        ).T




    #####################################
    # Fraud Detection
    #####################################



    def detect_fraud(self):



        fraud=[]



        for person in self.records:



            k=self.records[person]



            if not k["pan_verified"]:



                fraud.append(


                {

                "name":

                person,



                "issue":

                "Invalid PAN"

                }

                )



            if not k["aadhaar_verified"]:



                fraud.append(


                {

                "name":

                person,



                "issue":

                "Invalid Aadhaar"

                }

                )



            if k["face_score"]<85:



                fraud.append(


                {

                "name":

                person,



                "issue":

                "Face Match Failed"

                }

                )



        return fraud
