
# smart_contract.py

from datetime import datetime
import pandas as pd



class SmartContract:



    def __init__(self):


        self.buyers_balance={

            "Niraj":20000000,

            "Amit":15000000,

            "Sarah":25000000,

            "Rahul":10000000

        }


        self.sellers_balance={

            "Rahul":5000000,

            "Amit":7000000,

            "Sarah":9000000,

            "Niraj":1000000

        }



        self.transactions=[]



        self.ownership_history={}





    #######################################
    # GET BALANCE
    #######################################


    def get_balance(

            self,

            person

    ):



        if person in self.buyers_balance:

            return self.buyers_balance[person]



        if person in self.sellers_balance:

            return self.sellers_balance[person]



        return 0





    #######################################
    # ESCROW
    #######################################



    def escrow_payment(

            self,

            buyer,

            amount

    ):



        if self.buyers_balance[buyer]>=amount:



            self.buyers_balance[buyer]-=amount



            return True



        else:



            return False




    #######################################
    # RELEASE PAYMENT
    #######################################



    def release_payment(

            self,

            seller,

            amount

    ):



        if seller not in self.sellers_balance:



            self.sellers_balance[seller]=0



        self.sellers_balance[seller]+=amount





    #######################################
    # REGISTER OWNERSHIP
    #######################################



    def register_property(


            self,

            property_id,

            owner

    ):



        self.ownership_history[property_id]=[


            {

            "owner":owner,

            "timestamp":

            str(datetime.now())

            }

        ]





    #######################################
    # CURRENT OWNER
    #######################################



    def get_current_owner(

            self,

            property_id

    ):



        if property_id not in self.ownership_history:


            return None



        return self.ownership_history[

        property_id

        ][-1]["owner"]






    #######################################
    # OWNERSHIP HISTORY
    #######################################



    def get_history(

            self,

            property_id

    ):



        if property_id not in self.ownership_history:



            return []



        return self.ownership_history[

        property_id

        ]






    #######################################
    # DOUBLE SELL FRAUD
    #######################################



    def detect_double_sell(


            self,

            property_id,

            seller

    ):



        owner=self.get_current_owner(

        property_id

        )



        if owner!=seller:



            return True



        return False






    #######################################
    # EXECUTE SMART CONTRACT
    #######################################



    def execute_contract(


            self,

            property_id,

            buyer,

            seller,

            amount

    ):




        ################################

        # DOUBLE SELL

        ################################



        fraud=self.detect_double_sell(

        property_id,

        seller

        )



        if fraud:



            return {


            "status":"FAILED",



            "reason":

            "DOUBLE SELL FRAUD DETECTED"


            }





        ################################

        # ESCROW

        ################################



        escrow=self.escrow_payment(

        buyer,

        amount

        )



        if escrow==False:



            return {


            "status":"FAILED",



            "reason":

            "INSUFFICIENT BALANCE"

            }






        ################################

        # PAYMENT

        ################################



        self.release_payment(

        seller,

        amount

        )





        ################################

        # OWNERSHIP

        ################################



        self.ownership_history[

        property_id

        ].append(



        {


        "owner":

        buyer,



        "timestamp":

        str(datetime.now())

        }



        )







        ################################

        # LOG

        ################################



        tx={



        "property_id":

        property_id,



        "buyer":

        buyer,



        "seller":

        seller,



        "amount":

        amount,



        "timestamp":

        str(datetime.now()),



        "status":

        "SUCCESS"



        }




        self.transactions.append(

        tx

        )




        return {


        "status":"SUCCESS",



        "message":

        "SMART CONTRACT EXECUTED"



        }






    #######################################
    # TRANSACTION TABLE
    #######################################



    def get_transactions_df(

            self

    ):



        return pd.DataFrame(

        self.transactions

        )






    #######################################
    # OWNERSHIP TABLE
    #######################################



    def ownership_df(


            self,

            property_id

    ):



        h=self.get_history(

        property_id

        )



        return pd.DataFrame(

        h

        )
