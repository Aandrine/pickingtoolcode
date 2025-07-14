
#Sascha Laube, Simon Eich
from tkinter.tix import IMAGETEXT
import customtkinter as customtkinter
from customtkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import pandas as pd
from datetime import datetime
import os
from datetime import datetime
import os
from fanucpy import Robot

class FanucError(Exception):
    pass


def file_browser():
# Funktion to get the wafer map
    global chip_quality_array
    print("Opening next UI")
    file = filedialog.askopenfile()
    if file:
        file_extension = os.path.splitext(file.name)[1]
        if file_extension == '.xlsx':
            df = pd.read_excel(file.name, header=None)
        elif file_extension == '.csv':
            df = pd.read_csv(file.name, header=None, delimiter=';')
        else:
            error_message = "File type is not supported, use .csv or .xlsx."

            return

        waver_typ = df.iloc[0, 1]
        wafer = df.iloc[1, 1]
        current_datetime = datetime.now()
        data_array = df.iloc[7:].to_numpy()

        quality_values = [str(row[1]) for row in data_array]
        chip_quantity = len(quality_values)

        chip_quantity_ = f"{chip_quantity:02}"
        good_chip_count = len([row for row in data_array if row[1] != '0' and row[1] != 0])
        good_chip_count_ = f"{good_chip_count:02}"

        cmd = f"setregister:{chip_quantity_}:{good_chip_count_}:{':'.join(quality_values)}"

        # Information zu Qualität wird in VAR gespeichert
        quality_values = [str(row[1]) for row in data_array]
        global chip_quality_array
        chip_quality_array = quality_values

        # Filter data_array for rows where the second column (Qualitaet) is 1
        if file_extension == '.xlsx':
            data_array = np.array([row for row in data_array if row[1] != 0])
        else:
            data_array = np.array([row for row in data_array if row[1] == '1'])


        ablagepunkt = [[0 for x in range(4)] for y in range(99)]
        for i in range(min(99, len(data_array))):
            for j in range(4):
                if i * 4 + j < len(data_array):
                    ablagepunkt[i][j] = data_array[i * 4 + j][0]

        ablagepunkt_indices = [(i, j) for i in range(99) for j in range(4) if ablagepunkt[i][j] != 0]
        ablagepunkt_index_1 = [index[0] + 1 for index in ablagepunkt_indices]
        ablagepunkt_index_2 = [index[1] + 1 for index in ablagepunkt_indices]

        waver_info_df = pd.DataFrame({
            'Waver Typ': [waver_typ] * len(data_array),
            'Wafer Nummer': [wafer] * len(data_array),
            'Chip Nummer': [row[0] for row in data_array],
            'Qualitaet': [row[1] for row in data_array],
            'Gel Pak Nummer': ablagepunkt_index_1,
            'Position auf Gel Pak': ablagepunkt_index_2,
            'Coordinates' : (1,0),
        })

        robot = Robot(
                    robot_model="Fanuc",
                    host="129.129.178.127",
                    port=18735,
                    ee_DO_type="RDO",
                    ee_DO_num=7,
                )
        try:
            print('works')
            response = robot.connect()
            print(response["msg"], "green" if response["success"] else "red")
        except:
            print('Robot connection failed!', color="red")


        if response["success"]:
            try:
                response = robot.setregister(cmd=cmd)
                message = f"Answer Code: {response['code']} und message: {response['msg']}"
                color = "green" if response['code'] == 0 else "red"
                print(message, color)
            except FanucError as e:
                print(str(e), color="red")
            finally:
                robot.disconnect()


        output_file_xlsx = f"{waver_typ}_Wafer_{wafer}_TESTINANDRINE22_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
        waver_info_df.to_excel(output_file_xlsx, index=False)

        output_file_csv = f"{waver_typ}_Wafer_{wafer}_TESTINGANDRINE22_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        waver_info_df.to_csv(output_file_csv, index=False)
        print(f"Files saved as {output_file_xlsx} and {output_file_csv}")
        return chip_quality_array

file_browser()