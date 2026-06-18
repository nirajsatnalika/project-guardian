# fraud_detector.py

import pandas as pd


class FraudDetector:


    def __init__(self):


        self.alerts=[]




    #########################################

    # ADD ALERT

    #########################################


    def add_alert(

            self,

            category,

            severity,

            message,

            details=None

    ):



        self.alerts.append(


        {

        "Category":

        category,



        "Severity":

        severity,



        "Message":

        message,



        "Details":

        details

        }

        )






    #########################################

    # BLOCKCHAIN VALIDATION

    #########################################



    def blockchain_check(

            self,

            blockchain

    ):



        errors=blockchain.validate_chain()



        for e in errors:



            self.add_alert(



            category="Blockchain",



            severity="HIGH",



            message=e["type"],



            details=e



            )






    #########################################

    # PROPERTY OWNERSHIP

    #########################################



    def ownership_check(

            self,

            smart_contract,

            property_id,

            seller

    ):



        owner=smart_contract.get_current_owner(

        property_id

        )



        if owner!=seller:



            self.add_alert(



            category="Ownership",



            severity="CRITICAL",



            message="DOUBLE SELL FRAUD",



            details={



            "Property":

            property_id,



            "Actual Owner":

            owner,



            "Claimed Seller":

            seller

            }



            )






    #########################################

    # TOKEN SUPPLY

    #########################################



    def token_supply_check(



            self,

            tokenization,

            property_id

    ):



        result=tokenization.detect_fraud(

        property_id

        )



        if result["fraud"]:



            self.add_alert(



            category="Tokenization",



            severity="CRITICAL",



            message="TOKEN SUPPLY MISMATCH",



            details={



            "Expected":

            result["expected"],



            "Actual":

            result["actual"]

            }



            )







    #########################################

    # KYC CHECK

    #########################################



    def kyc_check(

            self,

            kyc

    ):



        fraud=kyc.detect_fraud()



        for f in fraud:



            self.add_alert(



            category="KYC",



            severity="MEDIUM",



            message=f["issue"],



            details=f

            )






    #########################################

    # PROPERTY VALUE FRAUD

    #########################################



    def value_fraud(



            self,

            market_value,

            declared_value

    ):



        diff=abs(

        market_value-declared_value

        )



        pct=diff/market_value




        if pct>0.30:



            self.add_alert(



            category="Property",



            severity="HIGH",



            message="SUSPICIOUS PROPERTY VALUATION",



            details={



            "Market":

            market_value,



            "Declared":

            declared_value,



            "Difference %":

            round(pct*100,2)

            }



            )







    #########################################

    # GET ALERTS

    #########################################



    def get_alerts(self):



        return self.alerts






    #########################################

    # ALERT TABLE

    #########################################



    def get_dataframe(self):



        if len(

        self.alerts

        )==0:



            return pd.DataFrame()



        return pd.DataFrame(

        self.alerts

        )







    #########################################

    # BLOCKCHAIN HEALTH SCORE

    #########################################



    def health_score(self):



        score=100




        for a in self.alerts:



            severity=a["Severity"]




            if severity=="MEDIUM":


                score-=10



            elif severity=="HIGH":


                score-=25




            elif severity=="CRITICAL":


                score-=40





        score=max(

        0,

        score

        )



        return score







    #########################################

    # HEALTH STATUS

    #########################################



    def health_status(self):



        score=self.health_score()




        if score>=90:


            return "EXCELLENT"



        elif score>=70:


            return "GOOD"



        elif score>=50:


            return "WARNING"



        else:


            return "CRITICAL"






    #########################################

    # RESET ALERTS

    #########################################



    def clear(self):



        self.alerts=[]
