
# tokenization.py

from datetime import datetime

import pandas as pd



class Tokenization:



    def __init__(self):



        self.properties={}



        self.transfer_history=[]




    ####################################################

    # TOKENIZE PROPERTY

    ####################################################



    def tokenize_property(


            self,

            property_id,

            property_name,

            property_value,

            total_tokens,

            owner

    ):




        token_price=property_value/total_tokens




        self.properties[property_id]={


        "property_name":

        property_name,



        "property_value":

        property_value,



        "total_tokens":

        total_tokens,



        "token_price":

        token_price,



        "holders":{


        owner:

        total_tokens

        }

        }




        return self.properties[property_id]







    ####################################################

    # GET HOLDERS

    ####################################################



    def get_holders(


            self,

            property_id

    ):



        if property_id not in self.properties:



            return {}



        return self.properties[

        property_id

        ]["holders"]







    ####################################################

    # TRANSFER TOKENS

    ####################################################



    def transfer_tokens(



            self,

            property_id,

            sender,

            receiver,

            amount

    ):




        holders=self.properties[

        property_id

        ]["holders"]





        ###################################

        # HOLDER EXIST

        ###################################



        if sender not in holders:



            return {



            "status":"FAILED",



            "reason":

            "Sender not found"

            }







        ###################################

        # BALANCE CHECK

        ###################################



        if holders[sender]<amount:



            return {


            "status":"FAILED",



            "reason":

            "Insufficient Tokens"

            }







        ###################################

        # TRANSFER

        ###################################



        holders[sender]-=amount




        if receiver not in holders:



            holders[receiver]=0





        holders[receiver]+=amount






        ###################################

        # HISTORY

        ###################################



        tx={



        "property_id":

        property_id,



        "sender":

        sender,



        "receiver":

        receiver,



        "tokens":

        amount,



        "timestamp":

        str(datetime.now())



        }




        self.transfer_history.append(

        tx

        )






        return {



        "status":"SUCCESS",



        "message":

        "Token Transfer Successful"

        }









    ####################################################

    # TOKEN SUPPLY CHECK

    ####################################################



    def validate_supply(

            self,

            property_id

    ):




        holders=self.properties[

        property_id

        ]["holders"]




        actual=sum(

        holders.values()

        )



        expected=self.properties[

        property_id

        ]["total_tokens"]





        if actual!=expected:




            return {



            "valid":

            False,



            "actual":

            actual,



            "expected":

            expected

            }





        return {



        "valid":

        True,



        "actual":

        actual,



        "expected":

        expected

        }







    ####################################################

    # FRAUD ATTEMPT

    ####################################################



    def inject_fake_tokens(



            self,

            property_id,

            fake_holder,

            amount

    ):




        holders=self.properties[

        property_id

        ]["holders"]




        holders[fake_holder]=amount




        return {

        "status":

        "FAKE TOKENS ADDED"

        }







    ####################################################

    # FRAUD DETECTOR

    ####################################################



    def detect_fraud(


            self,

            property_id

    ):




        result=self.validate_supply(

        property_id

        )





        if result["valid"]==False:



            return {



            "fraud":

            True,



            "message":

            "TOKEN SUPPLY MISMATCH",



            "expected":

            result["expected"],



            "actual":

            result["actual"]



            }







        return {



        "fraud":

        False,



        "message":

        "NO FRAUD"



        }









    ####################################################

    # HOLDERS TABLE

    ####################################################



    def holders_df(

            self,

            property_id

    ):



        holders=self.get_holders(

        property_id

        )




        rows=[]




        for holder,tokens in holders.items():



            rows.append(



            {

            "Holder":

            holder,



            "Tokens":

            tokens

            }



            )




        return pd.DataFrame(

        rows

        )









    ####################################################

    # TRANSFER HISTORY

    ####################################################



    def transfer_df(self):



        return pd.DataFrame(

        self.transfer_history

        )
