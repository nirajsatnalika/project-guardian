
# app.py


import streamlit as st

import pandas as pd

from blockchain import Blockchain

from kyc import KYC

from smart_contract import SmartContract

from tokenization import Tokenization

from fraud_detector import FraudDetector

from graph_utils import *





#####################################################

# PAGE CONFIG

#####################################################


st.set_page_config(

page_title="Project Guardian",

page_icon="🏠",

layout="wide"

)





#####################################################

# SESSION STATE

#####################################################



if "blockchain" not in st.session_state:


    st.session_state.blockchain=Blockchain()



bc=st.session_state.blockchain





if "kyc" not in st.session_state:


    st.session_state.kyc=KYC()



kyc=st.session_state.kyc






if "contract" not in st.session_state:


    st.session_state.contract=SmartContract()



contract=st.session_state.contract






if "token" not in st.session_state:


    st.session_state.token=Tokenization()



token=st.session_state.token







if "fraud" not in st.session_state:


    st.session_state.fraud=FraudDetector()



fraud=st.session_state.fraud






if "properties" not in st.session_state:


    st.session_state.properties={}





properties=st.session_state.properties







#####################################################

# TITLE

#####################################################



st.title(

"🏠 Project Guardian"

)



st.subheader(

"Blockchain Based Real Estate Fraud Prevention Platform"

)





st.markdown(

"""

This demo shows how Blockchain can help prevent:

- Fake Property Ownership

- Double Selling

- Document Manipulation

- KYC Fraud

- Token Supply Fraud

- Property Tokenization Fraud


"""

)





#####################################################

# SIDEBAR

#####################################################



st.sidebar.title(

"Navigation"

)





menu=st.sidebar.radio(



"Select Module",



[

"Dashboard",

"Register Property",

"Property List",

"Digital KYC",

"Smart Contract",

"Blockchain Ledger",

"Ownership History",

"Tokenization",

"Token Transfer",

"Fraud Demo",

"Fraud Dashboard"

]


)







#####################################################

# HELPER FUNCTIONS

#####################################################



def blockchain_health():



    if bc.is_valid():



        return "VALID"



    else:



        return "COMPROMISED"






def total_property_value():



    total=0



    for p in properties.values():



        total+=p["value"]



    return total







def total_tokens():



    total=0



    for p in token.properties:



        total+=token.properties[p][

        "total_tokens"

        ]



    return total







#####################################################

# DASHBOARD

#####################################################



if menu=="Dashboard":




    st.header(

    "📊 Dashboard"

    )





    col1,col2,col3,col4=st.columns(4)





    col1.metric(



    "Properties Registered",



    len(properties)

    )






    col2.metric(



    "Blockchain Blocks",



    len(

    bc.chain

    )



    )







    col3.metric(



    "Blockchain Status",



    blockchain_health()



    )







    col4.metric(



    "Total Property Value",



    f"₹ {total_property_value():,.0f}"



    )







    st.markdown(

    "---"

    )






    c1,c2=st.columns(2)






    with c1:




        st.metric(



        "Tokenized Assets",



        len(

        token.properties

        )



        )






        st.metric(



        "Total Tokens",



        total_tokens()



        )








    with c2:




        score=fraud.health_score()




        status=fraud.health_status()




        st.metric(



        "Blockchain Health Score",



        score



        )




        st.metric(



        "Risk Status",



        status



        )






    st.markdown(

    "---"

    )





    st.subheader(

    "Platform Capabilities"

    )






    st.write(



    "✅ Property Registry"

    )



    st.write(



    "✅ Digital KYC"

    )



    st.write(



    "✅ Smart Contracts"

    )



    st.write(



    "✅ Blockchain Ledger"

    )



    st.write(



    "✅ Property Tokenization"

    )



    st.write(



    "✅ Token Transfer"

    )



    st.write(



    "✅ Fraud Detection"

    )



    st.write(



    "✅ Blockchain Graph"

    )



#####################################################

# REGISTER PROPERTY

#####################################################


if menu=="Register Property":


    st.header(

    "🏠 Register Property"

    )



    col1,col2=st.columns(2)



    with col1:



        property_id=st.text_input(

        "Property ID",

        "PR101"

        )



        property_name=st.text_input(

        "Property Name",

        "Green Acres"

        )



        owner=st.text_input(

        "Owner",

        "Rahul"

        )




    with col2:



        location=st.text_input(

        "Location",

        "Mumbai"

        )



        value=st.number_input(

        "Market Value",

        value=10000000

        )



        area=st.number_input(

        "Area (sq ft)",

        value=1200

        )





    if st.button(

    "Register Property"

    ):




        #################################

        # DUPLICATE CHECK

        #################################



        if property_id in properties:



            fraud.add_alert(



            category="Property",



            severity="HIGH",



            message="DUPLICATE PROPERTY ID",



            details={

            "property_id":

            property_id

            }

            )



            st.error(

            "Duplicate Property ID"

            )





        else:




            properties[property_id]={



            "property_id":

            property_id,



            "property_name":

            property_name,



            "owner":

            owner,



            "location":

            location,



            "value":

            value,



            "area":

            area

            }






            contract.register_property(

            property_id,

            owner

            )






            bc.add_block(

            {

            "transaction":

            "PROPERTY REGISTERED",



            "property_id":

            property_id,



            "property_name":

            property_name,



            "owner":

            owner,



            "location":

            location,



            "value":

            value

            }

            )





            st.success(

            "Property Registered Successfully"

            )






            st.code(

            bc.latest_block().hash

            )



            st.write(

            "Blockchain Updated"

            )








#####################################################

# PROPERTY LIST

#####################################################


if menu=="Property List":



    st.header(

    "📋 Property Registry"

    )



    if len(properties)==0:



        st.warning(

        "No Properties Registered"

        )



    else:




        search=st.text_input(

        "Search Property ID"

        )






        rows=[]




        for pid,p in properties.items():



            if search=="":



                rows.append(p)



            else:



                if search.lower() in pid.lower():



                    rows.append(p)






        df=pd.DataFrame(

        rows

        )






        st.dataframe(

        df,

        use_container_width=True

        )







        st.markdown(

        "---"

        )







        st.subheader(

        "Property Statistics"

        )






        c1,c2,c3=st.columns(3)






        c1.metric(



        "Properties",



        len(properties)



        )






        total=0



        for p in properties.values():



            total+=p["value"]






        c2.metric(



        "Portfolio Value",



        f"₹ {total:,.0f}"



        )







        avg=0



        if len(properties)>0:



            avg=total/len(properties)







        c3.metric(



        "Average Property Value",



        f"₹ {avg:,.0f}"



        )








        ####################################

        # PROPERTY VALUE CHART

        ####################################





        chart=[]





        for p in properties.values():



            chart.append(



            {

            "Property":

            p["property_id"],



            "Value":

            p["value"]

            }



            )






        chart_df=pd.DataFrame(

        chart

        )







        st.bar_chart(



        chart_df.set_index(

        "Property"

        )



        )









#####################################################

# PROPERTY DETAILS

#####################################################



        st.markdown(

        "---"

        )



        st.subheader(

        "Property Details"

        )





        selected=st.selectbox(



        "Choose Property",



        list(

        properties.keys()

        )



        )






        p=properties[selected]







        st.write(

        "Property Name :",

        p["property_name"]

        )




        st.write(

        "Owner :",

        p["owner"]

        )



        st.write(

        "Location :",

        p["location"]

        )




        st.write(

        "Area :",

        p["area"]

        )




        st.write(

        "Value :",

        p["value"]

        )






        ###################################

        # BLOCKCHAIN HASH

        ###################################




        block_hash=None




        for b in bc.chain:



            if isinstance(

            b.data,

            dict

            ):



                if b.data.get(

                "property_id"

                )==selected:



                    block_hash=b.hash







        if block_hash:



            st.success(

            "Blockchain Verified"

            )



            st.code(

            block_hash

            )






        else:



            st.error(

            "Hash Not Found"

            )



#####################################################

# DIGITAL KYC

#####################################################


if menu=="Digital KYC":


    st.header(

    "🪪 Digital KYC Verification"

    )



    c1,c2=st.columns(2)




    with c1:



        name=st.text_input(

        "Full Name",

        "Rahul Sharma"

        )



        pan=st.text_input(

        "PAN",

        "ABCDE1234F"

        )



        aadhaar=st.text_input(

        "Aadhaar",

        "123456789012"

        )





    with c2:



        email=st.text_input(

        "Email",

        "rahul@gmail.com"

        )



        st.file_uploader(

        "Upload Selfie",

        type=["png","jpg","jpeg"]

        )



        st.file_uploader(

        "Upload PAN",

        type=["pdf","png","jpg"]

        )





    if st.button(

    "Verify KYC"

    ):




        result=kyc.verify_kyc(

        name,

        pan,

        aadhaar,

        email

        )






        ##################################

        # BLOCKCHAIN ENTRY

        ##################################




        bc.add_block(



        {

        "transaction":"KYC",



        "name":

        name,



        "pan":

        pan,



        "status":

        result["status"]

        }



        )








        if result["status"]=="VERIFIED":




            st.success(

            "KYC VERIFIED"

            )





            c1,c2,c3=st.columns(3)






            c1.metric(



            "PAN",



            "VERIFIED"

            )






            c2.metric(



            "AADHAAR",



            "VERIFIED"

            )







            c3.metric(



            "FACE MATCH",



            f"{result['face_score']}%"

            )






            st.code(

            bc.latest_block().hash

            )





            st.success(

            "Blockchain Updated"

            )







        else:




            st.error(

            "KYC FAILED"

            )








#####################################################

# KYC REGISTRY

#####################################################




    st.markdown(

    "---"

    )





    st.subheader(

    "KYC Registry"

    )





    kyc_df=kyc.get_dataframe()




    if len(

    kyc_df

    )>0:




        st.dataframe(



        kyc_df,



        use_container_width=True



        )






    else:



        st.info(

        "No KYC Records"

        )








#####################################################

# KYC STATISTICS

#####################################################




    if len(

    kyc.records

    )>0:




        verified=0



        failed=0





        for person in kyc.records:



            r=kyc.records[person]



            if r["status"]=="VERIFIED":



                verified+=1



            else:



                failed+=1







        st.markdown(

        "---"

        )






        a,b,c=st.columns(3)






        a.metric(



        "Total KYC",



        len(

        kyc.records

        )



        )







        b.metric(



        "Verified",



        verified



        )







        c.metric(



        "Failed",



        failed



        )










#####################################################

# KYC FRAUD DETECTION

#####################################################





    st.markdown(

    "---"

    )






    st.subheader(

    "🚨 KYC Fraud Detection"

    )






    frauds=kyc.detect_fraud()






    if len(

    frauds

    )==0:




        st.success(

        "No KYC Fraud Detected"

        )






    else:




        for f in frauds:




            fraud.add_alert(



            category="KYC",



            severity="MEDIUM",



            message=f["issue"],



            details=f

            )






            st.markdown(



            f"""



            <div style='



            background:#ffe6e6;



            border-left:10px solid red;



            padding:20px;



            border-radius:10px;



            margin-bottom:15px;



            '>





            <h3>

            KYC FRAUD ALERT

            </h3>





            Name :

            {f['name']}





            <br><br>





            Issue :

            {f['issue']}





            </div>





            """,



            unsafe_allow_html=True



            )









#####################################################

# BLOCKCHAIN KYC HISTORY

#####################################################





    st.markdown(

    "---"

    )





    st.subheader(

    "Blockchain KYC Records"

    )






    rows=[]






    for b in bc.chain:




        if isinstance(

        b.data,

        dict

        ):




            if b.data.get(

            "transaction"

            )=="KYC":




                rows.append(

                {

                "Block":

                b.index,



                "Name":

                b.data["name"],



                "PAN":

                b.data["pan"],



                "Status":

                b.data["status"],



                "Hash":

                b.hash[:20]

                }

                )








    if len(

    rows

    )>0:




        df=pd.DataFrame(

        rows

        )




        st.dataframe(



        df,



        use_container_width=True



        )






    else:




        st.info(

        "No Blockchain KYC Records"

        )



#####################################################

# SMART CONTRACT

#####################################################


if menu=="Smart Contract":



    st.header(

    "🤝 Smart Contract Execution"

    )



    if len(properties)==0:



        st.warning(

        "Register Property First"

        )



    else:



        property_id=st.selectbox(


        "Select Property",


        list(

        properties.keys()

        )



        )





        p=properties[property_id]



        current_owner=p["owner"]





        c1,c2=st.columns(2)





        with c1:



            st.write(

            "Property :",

            p["property_name"]

            )



            st.write(

            "Current Owner :",

            current_owner

            )



            st.write(

            "Location :",

            p["location"]

            )





        with c2:



            st.write(

            "Value :",

            f"₹ {p['value']:,.0f}"

            )



            st.write(

            "Area :",

            p["area"]

            )






        st.markdown(

        "---"

        )






        buyer=st.selectbox(



        "Buyer",



        [

        "Niraj",

        "Amit",

        "Sarah",

        "Rahul"

        ]



        )







        seller=st.text_input(



        "Seller",



        current_owner



        )







        amount=st.number_input(



        "Sale Amount",



        value=int(

        p["value"]

        )



        )









        st.markdown(

        "### Buyer Balance"

        )







        st.metric(



        buyer,



        f"₹ {contract.get_balance(buyer):,.0f}"



        )








        if st.button(



        "Execute Smart Contract"



        ):







            result=contract.execute_contract(



            property_id,



            buyer,



            seller,



            amount



            )








            if result["status"]=="SUCCESS":






                ################################

                # UPDATE PROPERTY OWNER

                ################################




                properties[property_id][

                "owner"

                ]=buyer







                ################################

                # BLOCKCHAIN

                ################################




                bc.add_block(




                {



                "transaction":

                "PROPERTY SALE",




                "property_id":

                property_id,




                "seller":

                seller,




                "buyer":

                buyer,




                "amount":

                amount




                }



                )








                st.success(



                "SMART CONTRACT EXECUTED"



                )








                a,b,c=st.columns(3)








                a.metric(



                "Escrow",



                "SUCCESS"



                )








                b.metric(



                "Payment",



                "RELEASED"



                )








                c.metric(



                "Ownership",



                "TRANSFERRED"



                )








                st.code(



                bc.latest_block().hash



                )







                st.success(



                "Blockchain Updated"



                )







            else:








                fraud.add_alert(




                category="Ownership",




                severity="CRITICAL",




                message=result["reason"],




                details={



                "property":

                property_id,



                "buyer":

                buyer,



                "seller":

                seller



                }



                )








                st.error(



                result["reason"]



                )









#####################################################

# TRANSACTION HISTORY

#####################################################




    st.markdown(

    "---"

    )







    st.subheader(

    "Transaction History"

    )







    tx=contract.get_transactions_df()








    if len(tx)>0:





        st.dataframe(



        tx,



        use_container_width=True



        )








    else:




        st.info(

        "No Transactions"

        )









#####################################################

# OWNERSHIP HISTORY

#####################################################





if menu=="Ownership History":






    st.header(

    "📜 Ownership History"

    )







    if len(properties)==0:





        st.warning(

        "No Properties"

        )







    else:







        property_id=st.selectbox(



        "Property",



        list(

        properties.keys()

        )



        )








        history=contract.ownership_df(

        property_id

        )









        if len(

        history

        )>0:








            st.dataframe(



            history,



            use_container_width=True



            )








            st.markdown(

            "---"

            )








            st.subheader(

            "Ownership Graph"

            )









            fig=ownership_graph(



            contract,



            property_id



            )








            st.pyplot(



            fig



            )








        else:





            st.info(

            "No Ownership History"

            )









#####################################################

# BLOCKCHAIN SALES

#####################################################





        st.markdown(

        "---"

        )







        st.subheader(

        "Blockchain Sale Records"

        )








        rows=[]








        for b in bc.chain:





            if isinstance(

            b.data,

            dict

            ):







                if b.data.get(

                "transaction"

                )=="PROPERTY SALE":








                    rows.append(




                    {



                    "Block":



                    b.index,





                    "Property":



                    b.data["property_id"],





                    "Seller":



                    b.data["seller"],





                    "Buyer":



                    b.data["buyer"],





                    "Amount":



                    b.data["amount"],





                    "Hash":



                    b.hash[:20]




                    }




                    )









        if len(rows)>0:






            df=pd.DataFrame(



            rows



            )








            st.dataframe(



            df,



            use_container_width=True



            )








        else:





            st.info(



            "No Blockchain Sales"



            )


#####################################################

# TOKENIZATION

#####################################################


if menu=="Tokenization":



    st.header(

    "🪙 Property Tokenization"

    )



    if len(properties)==0:



        st.warning(

        "Register Property First"

        )



    else:




        property_id=st.selectbox(



        "Select Property",



        list(

        properties.keys()

        )



        )





        p=properties[property_id]






        st.write(

        "Property :",

        p["property_name"]

        )



        st.write(

        "Owner :",

        p["owner"]

        )



        st.write(

        "Value :",

        f"₹ {p['value']:,.0f}"

        )








        total_tokens=st.number_input(



        "Total Tokens",



        value=1000



        )








        if st.button(



        "Tokenize Property"



        ):







            result=token.tokenize_property(



            property_id,



            p["property_name"],



            p["value"],



            total_tokens,



            p["owner"]



            )








            bc.add_block(




            {



            "transaction":

            "TOKENIZATION",




            "property_id":

            property_id,




            "owner":

            p["owner"],




            "tokens":

            total_tokens




            }




            )








            st.success(



            "PROPERTY TOKENIZED"



            )








            c1,c2=st.columns(2)








            c1.metric(



            "Total Tokens",



            total_tokens



            )








            c2.metric(



            "Token Price",



            f"₹ {result['token_price']:,.0f}"



            )








            st.code(



            bc.latest_block().hash



            )








            st.success(



            "Blockchain Updated"



            )










#####################################################

# TOKEN OWNERSHIP

#####################################################




    st.markdown(

    "---"

    )







    st.subheader(

    "Token Ownership"

    )








    if property_id in token.properties:








        st.dataframe(



        token.holders_df(

        property_id

        ),



        use_container_width=True



        )








        st.markdown(

        "---"

        )








        st.subheader(

        "Ownership Network"

        )








        fig=token_graph(



        token,



        property_id



        )








        st.pyplot(



        fig



        )










#####################################################

# TOKEN TRANSFER

#####################################################



if menu=="Token Transfer":





    st.header(

    "🔁 Transfer Tokens"

    )







    if len(

    token.properties

    )==0:





        st.warning(

        "Tokenize Property First"

        )








    else:








        property_id=st.selectbox(



        "Property",



        list(

        token.properties.keys()

        )



        )








        holders=token.get_holders(

        property_id

        )








        sender=st.selectbox(



        "Sender",



        list(

        holders.keys()

        )



        )








        receiver=st.text_input(



        "Receiver",



        "Niraj"



        )








        amount=st.number_input(



        "Tokens",



        value=100



        )









        st.metric(



        "Available Tokens",



        holders[sender]



        )










        if st.button(



        "Transfer"



        ):







            result=token.transfer_tokens(



            property_id,



            sender,



            receiver,



            amount



            )








            if result["status"]=="SUCCESS":







                bc.add_block(




                {



                "transaction":

                "TOKEN TRANSFER",




                "property_id":

                property_id,




                "sender":

                sender,




                "receiver":

                receiver,




                "tokens":

                amount




                }




                )








                st.success(



                "TOKEN TRANSFER SUCCESSFUL"



                )








                st.code(



                bc.latest_block().hash



                )








                st.dataframe(



                token.holders_df(

                property_id

                ),



                use_container_width=True



                )








            else:








                st.error(



                result["reason"]



                )









#####################################################

# TOKEN TRANSFER HISTORY

#####################################################






    st.markdown(

    "---"

    )








    st.subheader(

    "Transfer History"

    )








    tx=token.transfer_df()








    if len(tx)>0:







        st.dataframe(



        tx,



        use_container_width=True



        )








    else:





        st.info(

        "No Transfers"

        )









#####################################################

# TOKEN FRAUD DEMO

#####################################################





if menu=="Fraud Demo":






    st.header(

    "🚨 Token Fraud Demo"

    )








    if len(

    token.properties

    )==0:





        st.warning(

        "Tokenize Property First"

        )








    else:








        property_id=st.selectbox(



        "Property",



        list(

        token.properties.keys()

        )



        )








        fake_holder=st.text_input(



        "Fake Holder",



        "John"



        )








        fake_tokens=st.number_input(



        "Fake Tokens",



        value=5000



        )









        if st.button(



        "Inject Fake Tokens"



        ):








            token.inject_fake_tokens(



            property_id,



            fake_holder,



            fake_tokens



            )








            fraud.token_supply_check(



            token,



            property_id



            )








            result=token.detect_fraud(



            property_id



            )









            st.error(



            "TOKEN FRAUD DETECTED"



            )










            st.markdown(



            f"""



            <div style='



            background:#ffe6e6;



            border-left:10px solid red;



            padding:25px;



            border-radius:10px;



            '>





            <h2>

            TOKEN SUPPLY MISMATCH

            </h2>





            Expected Tokens :



            {result['expected']}





            <br><br>





            Actual Tokens :



            {result['actual']}





            <br><br>





            Fraud Holder :



            {fake_holder}





            </div>





            """,



            unsafe_allow_html=True



            )









            st.dataframe(



            token.holders_df(

            property_id

            ),



            use_container_width=True



            )










            st.markdown(

            "---"

            )










            st.subheader(

            "Fraud Network"

            )










            fig=token_fraud_graph(



            token,



            property_id,



            fake_holder



            )










            st.pyplot(

            fig

            )



#####################################################

# BLOCKCHAIN LEDGER

#####################################################


if menu=="Blockchain Ledger":


    st.header(

    "⛓️ Blockchain Ledger"

    )



    st.subheader(

    "Ledger Records"

    )



    ledger=bc.get_chain_dataframe()



    st.dataframe(

    ledger,

    use_container_width=True

    )



    st.markdown(

    "---"

    )



    st.subheader(

    "Blockchain Network"

    )



    fig=blockchain_graph(

    bc

    )



    st.pyplot(

    fig

    )





    ###################################

    # TAMPERING

    ###################################



    st.markdown(

    "---"

    )



    st.subheader(

    "🚨 Blockchain Tampering Demo"

    )



    tamper_block=st.number_input(

    "Block Number",

    min_value=1,

    max_value=max(

    1,

    len(bc.chain)-1

    ),

    value=1

    )



    fake_owner=st.text_input(

    "Fake Owner",

    "John"

    )





    if st.button(

    "Tamper Blockchain"

    ):





        try:



            b=bc.chain[

            tamper_block

            ]





            if isinstance(

            b.data,

            dict

            ):





                b.data["owner"]=fake_owner





                st.warning(

                "Block Modified"

                )



                st.write(

                "Hash NOT updated"

                )





        except:



            st.error(

            "Unable to Tamper"

            )







    ##################################

    # VALIDATION

    ##################################





    errors=bc.validate_chain()







    if len(

    errors

    )==0:





        st.success(

        "Blockchain Valid"

        )







    else:






        st.error(

        "Blockchain Compromised"

        )







        fraud_blocks=[]






        for e in errors:





            fraud_blocks.append(

            e["block"]

            )







            fraud.add_alert(




            category="Blockchain",




            severity="CRITICAL",




            message=e["type"],




            details=e




            )







            st.markdown(




            f"""



            <div style='



            background:#ffe6e6;



            border-left:10px solid red;



            padding:20px;



            border-radius:10px;



            margin-bottom:20px;



            '>





            <h2>

            BLOCK {e['block']}

            </h2>





            <b>

            {e['type']}

            </b>





            <br><br>





            Stored Hash

            <br>



            {e.get(

            'stored_hash',

            '-'

            )}





            <br><br>





            Expected Hash

            <br>



            {e.get(

            'expected_hash',

            '-'

            )}






            </div>





            """,



            unsafe_allow_html=True



            )








        st.markdown(

        "---"

        )







        st.subheader(

        "Compromised Blockchain"

        )







        fig=blockchain_fraud_graph(

        bc,

        fraud_blocks

        )







        st.pyplot(

        fig

        )









#####################################################

# FRAUD DASHBOARD

#####################################################





if menu=="Fraud Dashboard":






    st.header(

    "🚨 Fraud Dashboard"

    )








    score=fraud.health_score()







    status=fraud.health_status()








    a,b,c=st.columns(3)








    a.metric(



    "Blockchain Health",



    score



    )








    b.metric(



    "Risk Status",



    status



    )








    c.metric(



    "Alerts",



    len(

    fraud.get_alerts()

    )



    )








    st.markdown(

    "---"

    )








    alerts=fraud.get_alerts()








    if len(

    alerts

    )==0:





        st.success(

        "No Fraud Detected"

        )








    else:








        for a in alerts:








            color="#ffe6e6"








            if a["Severity"]=="MEDIUM":



                color="#fff7cc"








            elif a["Severity"]=="HIGH":



                color="#ffd9b3"








            elif a["Severity"]=="CRITICAL":



                color="#ffe6e6"









            st.markdown(




            f"""



            <div style='



            background:{color};



            border-left:10px solid red;



            padding:25px;



            border-radius:10px;



            margin-bottom:20px;



            '>





            <h3>

            {a['Severity']}

            </h3>





            Category :



            {a['Category']}





            <br><br>





            Message :



            {a['Message']}





            <br><br>





            Details :



            {a['Details']}





            </div>





            """,



            unsafe_allow_html=True



            )








    st.markdown(

    "---"

    )








    st.subheader(

    "Alert Table"

    )








    df=fraud.get_dataframe()








    if len(

    df

    )>0:







        st.dataframe(



        df,



        use_container_width=True



        )


