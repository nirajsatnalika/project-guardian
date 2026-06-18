
# blockchain.py

import hashlib

import json

from datetime import datetime



class Block:


    def __init__(

            self,

            index,

            timestamp,

            data,

            previous_hash

    ):


        self.index=index

        self.timestamp=timestamp

        self.data=data

        self.previous_hash=previous_hash

        self.hash=self.calculate_hash()



    def calculate_hash(self):


        block_string=json.dumps(

        {

        "index":self.index,

        "timestamp":self.timestamp,

        "data":self.data,

        "previous_hash":self.previous_hash

        },

        sort_keys=True

        )



        return hashlib.sha256(

        block_string.encode()

        ).hexdigest()




class Blockchain:



    def __init__(self):


        self.chain=[]


        self.create_genesis_block()




    def create_genesis_block(self):


        genesis=Block(

        0,

        str(datetime.now()),

        {

        "transaction":

        "Genesis Block"

        },

        "0"

        )


        self.chain.append(genesis)





    def latest_block(self):


        return self.chain[-1]





    def add_block(

            self,

            data

    ):



        prev=self.latest_block()



        new_block=Block(

        len(self.chain),

        str(datetime.now()),

        data,

        prev.hash

        )



        self.chain.append(

        new_block

        )





    def validate_chain(self):



        errors=[]



        for i in range(

        1,

        len(self.chain)

        ):



            curr=self.chain[i]


            prev=self.chain[i-1]



            recalculated=curr.calculate_hash()



            if curr.hash!=recalculated:



                errors.append(


                {

                "block":i,

                "type":"HASH MISMATCH",

                "stored_hash":

                curr.hash,

                "expected_hash":

                recalculated

                }

                )



            if curr.previous_hash!=prev.hash:



                errors.append(


                {

                "block":i,

                "type":"PREVIOUS HASH BROKEN",

                "stored_previous":

                curr.previous_hash,

                "actual_previous":

                prev.hash

                }

                )




        return errors





    def is_valid(self):


        return len(

        self.validate_chain()

        )==0




    def get_chain_dataframe(self):



        import pandas as pd



        rows=[]



        for b in self.chain:



            rows.append(


            {

            "Block":

            b.index,



            "Timestamp":

            b.timestamp,



            "Transaction":

            b.data.get(

            "transaction",

            "-"

            )

            if isinstance(

            b.data,

            dict

            )

            else

            b.data,



            "Property":

            b.data.get(

            "property_id",

            "-"

            )

            if isinstance(

            b.data,

            dict

            )

            else

            "-",



            "Hash":

            b.hash[:20],



            "Previous":

            b.previous_hash[:20]

            }

            )



        return pd.DataFrame(

        rows

        )
