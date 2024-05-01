import socket
import time 
import streamlit as st

host="10.0.0.102"
port = 5555

# button_counter = 0
send_command = False
st.title("Motor-Sliders for Robot's face")



def send_commands():
    # while send_command:
        # to_be_sent = {9:val_9, 10:val_10, 11:val_11, 12:val_12, 13:val_13, 14:val_14, 15:val_15}
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            print("########")
            # time.sleep(0.4)
            for key, value in to_be_sent.items():
                command = f"!dsl2:{key}={value}#"
                try:
                    print(command)
                    s.sendto(command.encode('utf-8'), (host, port))
                except Exception as e:
                    print(e)
            print("*********")


# sliders for recording the value to be sent to the motors
val_9 = st.slider('9-Jaw', min_value=0, max_value=1000, step=1, on_change=send_commands)
val_10 = st.slider('10-Upper Lip Left', min_value=0, max_value=1000, step=1, on_change=send_commands)
val_11 = st.slider('11-Upper Lip Right', min_value=0, max_value=1000, step=1, on_change=send_commands)
val_12 = st.slider('12-Lower Lip Right', min_value=0, max_value=1000, step=1, on_change=send_commands)
val_13 = st.slider('13-Lower Lip Left', min_value=0, max_value=1000, step=1, on_change=send_commands)
val_14 = st.slider('14-Cheek Left', min_value=0, max_value=1000, step=1, on_change=send_commands)
val_15 = st.slider('15-Cheek Right', min_value=0, max_value=1000, step=1, on_change=send_commands)
st.write(f"[9: {val_9}, 10: {val_10}, 11: {val_11}, 12: {val_12}, 13: {val_13}, 14: {val_14}, 15: {val_15}]")
to_be_sent = {9:val_9, 10:val_10, 11:val_11, 12:val_12, 13:val_13, 14:val_14, 15:val_15}



# # button to control the commands being sent to the motors or now
power_button = st.button("Start/Stop")
if power_button:
    if send_command: 
        send_command = False
    else:
        send_command = True
        send_commands()
